from app import db

# Your database models should go here.
# Check out the Flask-SQLAlchemy quickstart for some good docs!
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/

tags = db.Table('club_tag',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), ),
    db.Column('club_id', db.Integer, db.ForeignKey('club.id'), )
    )
    #many-to-many tabel to map club.id to tag.id

class Club(db.Model):
    __tablename__ = "club"
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=True)

    tags = db.relationship("Tag", backref=db.backref("club", lazy=True))

    def __init__(self, code, name, description):
        self.code = code
        self.name = name
        self.description = description


class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=False, nullable=False)

    def __init__(self, name):
        self.name = name


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    user_name = db.Column(db.String(30), unique=False, nullable=False)

    posts = db.relationship('Post', backref='author', lazy=True) 
    #one-to many relationship between user and posts
    #could input many-many table with user.id and club.id
    #reviews posted under user.user_name?

    def __repr__(self):
        return f"User('{self.user_name}', '{self.name}')"

    def __init__(self, name, user_name):
        self.name = name
        self.user_name = user_name

class Post(db.Model):
    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=False, nullable=False)
    content = db.Column(db.Text, unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)