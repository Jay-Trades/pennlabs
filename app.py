from flask import Flask, request, jsonify
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


@app.route('/api/clubs', methods=['GET'])
def show_clubs():
    clubs = Club.query.all()
    return jsonify([club.serialize() for club in clubs])

@app.route('/api/user/<username>', methods=['GET'])
def get_profile(username):
    profile = User.query.filter_by(user_name=username).first()
    return jsonify(profile.serialize())
    #need to add the serialize function into each function to return json like dict objs


@app.route('/api/clubs?search=<QUERY>', methods=['GET'])
def get_club(QUERY):
    name = str(QUERY).lower()
    return name
    # Club.query.filter_by(name={name})   #I could get all the club names and see if the name is in club_name
    # clubs = Club.query.filter(Club.name.like("%{}%".format(name))).all()
    # return jsonify([club.serialize() for club in clubs])


@app.route('/api/clubs', methods=['POST'])
def post_club():
    data = request.get_json()
    club = Club(name=data["name"], code=data["code"], description=data["description"])
    db.session.add(club)
    db.session.commit()

#this will get the json data and i can assume that each field will have the speciified data


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
        else:
            for club in tag.club:
                count[tag.name] += 1
                
    for k, v in count:
        result.append({"tag": k, "count":v}

    return jsonify(result)

if __name__ == '__main__':
    app.run()
