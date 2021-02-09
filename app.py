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
        clubs = Club.query.all()    #returns all clubs objs in a list
        return jsonify([club.serialize() for club in clubs])
        #serialize all clubs in json format then return
    else:
        data = request.get_json()   #this will get the json data and i can assume that each field will have the speciified data
        club = Club(name=data["name"], code=data["code"], description=data["description"])
        db.session.add(club)
        db.session.commit()
        return Response(status=201)

@app.route('/api/user/<username>', methods=['GET'])
def get_profile(username):
    profile = User.query.filter_by(user_name=username).first()  #get user obj by username
    return jsonify(profile.serialize())


@app.route('/api/clubs', methods=['GET'])
def get_club():
    name = request.args.get('search')
    arg = "%"+name+"%"                              #syntax for finding strings that include the arg in it
    clubs = Club.query.filter(Club.name.like(arg)).all()    #filters club names that have the arg in it
    return jsonify([club.serialize() for club in clubs])

@app.route('/api/clubs/:code', methods=['PATCH'])   #not sure if :code was the parameter for querying the club
def modify():
    data = request.get_json()
    club = Club.query.filter_by(code=data['code'])  #find the club with the give code arg
    for k, v in data:
        if data[k]:                                 #only modify the data if the args are not empty.
            if k == 'name':
                club.name = v
            elif k == 'description':
                club.description = v
            elif k == 'code':
                club.code = v
    db.session.commit()

@app.route('/api/tag_count', methods=['GET'])
def get_tag():
    tags = Tag.query.all()  #get all tags
    count = {}
    result = []
    for tag in tags:    #iterate through all tags and create dictionary with tag.name as key
        count[tag.name] = 0
        for club in tag.club:   #increment count for every club in tag.club (all clubs associated with that tag)
            count[tag.name] += 1
                
    for k, v in count:
        result.append({"tag": k, "count": v}) #seralize the result 

    return jsonify(result)

@app.route('/api/:club/favorite', methods=['POST'])
def favorite():
    data = request.get_json()
    club_name = data['club']
    user_name = data['user']
    user = User.query.filter_by(user_name=user_name).first()    #finds the user by user_name
    exist = user.favorites.query.filter_by(club=club_name).first()  #trys to find the club in users favorite clubs (user.favorites)
    if not exist:                                                   #if exist is none we add the club to user.favorites
        club = Club.query.filter_by(name=club_name).first()
        user.favorites.append(club)
        db.session.commit()
        return Response(status=201)

    else:
        return "You already favorited that club!"

if __name__ == '__main__':
    app.run()
