import os
import json

def load_data():
    with open('clubs.json') as json_file:
        data = json.load(json_file)

    seen = {}
    for item in data:
        code = item.get("code")
        name = item.get("name")
        description = item.get("description")
        print(code, name, description)

        tags = item.get("tags")#if the tags are a list of strings
        for tag in tags:
            if tag not in seen:
                seen[tag] = True
                print(tag)

load_data()