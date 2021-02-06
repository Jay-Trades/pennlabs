import os
import json
from app import db, DB_FILE
from models import *


def create_user():
    person = User(user_name="josh", name="Josh L")
    db.session.add(person)
    db.session.commit()
    print("TODO: Create a user called josh")


def load_data():
    with open('clubs.json') as json_file:
        data = json.load(json_file)

    seen = {}
    for item in data:
        code = item.get("code")
        name = item.get("name")
        description = item.get("description")
        club = Club(code = code, name = name, description= description)
        db.seesion.add(club)

        tags = item.get("tags")#if the tags are a list of strings
        for tag in tags:
            if tag not in seen:
                seen[tag] = True
                tag_to_add = Tag(name = tag)
                db.seesion.add(tag_to_add)

    db.session.commit()
    print("TODO: Load in clubs.json to the database.")


# No need to modify the below code.
if __name__ == '__main__':
    # Delete any existing database before bootstrapping a new one.
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)

    db.create_all()
    #create_user()
    load_data()
