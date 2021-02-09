# Penn Labs Backend Challenge

## Documentation

See File structure to see how db is modeled.
Implemented a `tag` table holds all the unique tags and `club` table for all unique clubs
Implemented a `club_tag` table, many-to-many relationship between `club` and `tag` because each club can have many tags and each tag can map to many clubs.
Same logic applies to `user_favorites` table it uses a Many-to-many relationship between `User` and `Club`.

## Installation

1. Install 'pipenv'. - `pip install --user --upgrade pipenv`
2. Intall packages flask, Flask SQLAlchemy, with `pipenv install`
3. Run `bootstrap.py` to create database, run `app.py` to start flask server.

## File Structure / functions

- `app.py`: Contains routes

   -/api/user/:username : get user profile
   -/api/club : get all exisiting clubs
   -/api/clubs?search=<QUERY> : get clubs with <QUERY> in name
   -/api/club : post add new club
   -/api/:club/favorite : post new favorite club
   -/api/tag_count : get tags and # of clubs associate with that tag


- `models.py`: Model definitions for SQLAlchemy database models. 

   -Club: table with fields (code, name, description)
      -`tags` is a Club attribute that repersents all tags a specific club maps to in the club_tag helper table

   -Tag: table with fields (name(tag name))
      -`club` is a Tag attribute that repersents all clubs a specific tag maps to in the club_tag helper table

   -club_tag: helper table with fields(club.id, tag.id)
      -This table repersents the many-to-many relationship between clubs and tags.

   -User: table with fields (name, user_name)

      -`favorite_clubs` is a User attribute that repersents all clubs a specific user maps to in the user_favorites helper table
      - Implemented a many-to-many table because each user can have multiple favorite clubs and a Club can have many Users favorites. 
      - Could add review attribute for future use and implement a reviews table to store user reviews. Which would map to clubs and user in a many to 1 relationship.

   -user_favorites: helper table with fields(club.id, user.id)
      -This table repersents the many-to-many relationship between clubs and user.


- `bootstrap.py`: Code for creating and populating your local database. Will add club.json into a sqlite db.

## Developing

0. Determine how to model the data contained within `clubs.json` and then complete `bootstrap.py`
1. Run `pipenv run python bootstrap.py` to create the database and populate it.
2. Use `pipenv run flask run` to run the project.
3. Follow the instructions [here](https://www.notion.so/pennlabs/Backend-Challenge-Fall-20-31461f3d91ad4f46adb844b1e112b100).
4. Document your work in this `README.md` file.

## Reference frontend

If you want to use the reference frontend to see if your implementation of the
backend is working correctly, follow the below steps

1. `cd reference-frontend` to enter the directory.
2. `yarn install` to download all the dependencies.
3. `yarn start` to start the server.
4. Navigate to `localhost:3000` to see if the website is working correctly.

Feel free to make changes to the reference frontend as necessary. If you want
to work on the reference frontend as a supplementary challenge, the current
implementation doesn't implement _tags_. Modifying the reference frontend to
list club tags while browsing clubs or allow users to include tags while
creating a new club could be a good place to start with improving the frontend.

## Submitting

Follow the instructions on the Technical Challenge page for submission.

## Installing Additional Packages

Use any tools you think are relevant to the challenge! To install additional packages
run `pipenv install <package_name>` within the directory. Make sure to document your additions.

