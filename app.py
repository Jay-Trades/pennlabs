from flask import Flask, request, jsonify, Response, render_template
from flask_sqlalchemy import SQLAlchemy
import json

DB_FILE = "clubreview.sqlite3"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_FILE}"
db = SQLAlchemy(app)

from models import *


@app.route('/')
def main():
    return "Welcome to Penn Club Review!"


@app.route('/api')
def api():
    return jsonify("Welcome to the Penn Club Review API!.")


@app.route('/api/club', methods=['GET', 'POST'])
def modify_clubs():
    if request.method == 'GET':
        clubs = Club.query.all()
        return jsonify([club.serialize() for club in clubs])
        #serialize all clubs in json format then return
    else:
        data = request.get_json()
        club = Club(name=data["name"], code=data["code"], description=data["description"])
        db.session.add(club)
        db.session.commit()
        return 201
        #this will get the json data and i can assume that each field will have the speciified data

@app.route('/api/user/<username>', methods=['GET'])
def get_profile(username):
    profile = User.query.filter_by(user_name=username).first()
    return jsonify(profile.serialize())


@app.route('/api/clubs', methods=['GET'])
def get_club():
    name = request.args.get('search')
    arg = "%"+name+"%"
    clubs = Club.query.filter(Club.name.like(arg)).all()
    return jsonify([club.serialize() for club in clubs])

@app.route('/api/clubs/:code', methods=['PATCH'])
def modify():
    data = request.get_json()
    club = Club.query.filter_by(code=data['code'])
    for k, v in data:
        if data[k]:
            if k == 'name':
                club.name = v
            elif k == 'description':
                club.description = v
            elif k == 'code':
                club.code = v


@app.route('/api/tag_count', methods=['GET'])
def get_tag():
    tags = Tag.query.all()
    count = {}
    result = []
    for tag in tags:
        if tag.name not in count:
            count[tag.name] = 0
            for club in tag.club:
                count[tag.name] += 1
                
    for k, v in count:
        result.append({"tag": k, "count":v})

    return jsonify(result)

@app.route('/api/:club/favorite', methods=['POST'])
def favorite():
    data = request.get_json()
    club_name = data['club']
    user_name = data['user']
    user = User.query.filter_by(user_name=user_name).first()
    exist = user.favorites.query.filter_by(club=club_name).first()
    if not exist:
        club = Club.query.filter_by(name=club_name).first()
        user.favorites.append(club)
    else:
        return "You already favorited that club!"

if __name__ == '__main__':
    app.run()
