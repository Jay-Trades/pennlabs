import os
import json
from app import db, DB_FILE


from models import *

def create_user():
    person = User(user_name="josh", name="Josh L")
    db.session.add(person)
    db.session.commit()


def load_data():
    with open('clubs.json') as json_file:
        data = json.load(json_file)

    for item in data:
        code = item.get("code")
        name = item.get("name")
        description = item.get("description")
        club = Club(code = code, name = name, description= description)

        tags = item.get("tags") #tags in a list of strings
        for tag_name in tags:
            tag_obj = Tag.query.filter_by(name=tag_name).first() #check if tag is in Tag table

            if not tag_obj: #if tag_obj none we add it to Tag table
                tag_to_add = Tag(name = tag_name)
                club.tags.append(tag_to_add)
                #adds tags that are unique
            else:
                club.tags.append(tag_obj)
                #specific instance of club in the tags table (many-to-many) append the tag obj
        db.session.add(club)
        db.session.commit()

# No need to modify the below code.
if __name__ == '__main__':
    # Delete any existing database before bootstrapping a new one.
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)

    db.create_all()
    create_user()
    load_data()
