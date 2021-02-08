from app import db

# Your database models should go here.
# Check out the Flask-SQLAlchemy quickstart for some good docs!
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/

club_tag = db.Table('club_tag',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('club_id', db.Integer, db.ForeignKey('club.id'))
    )
    #many-to-many tabel to map club.id to tag.id

# class Link(db.Model):
#     __tablename__ = 'link'
#     tag_id = db.Column(
#       db.Integer, 
#       db.ForeignKey('tag.id'), 
#       primary_key = True)

#     club_id = db.Column(
#     db.Integer, 
#     db.ForeignKey('club.id'), 
#     primary_key = True)

class Club(db.Model):
    __tablename__ = "club"
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(300), unique=False, nullable=True)

    #tags = db.relationship("Tag", secondary="club_tag", backref=db.backref("club", lazy=True))
    tags = db.relationship("Tag", secondary="club_tag", backref="club")

    def __init__(self, code, name, description):
        self.code = code
        self.name = name
        self.description = description

    def serialize(self):
        return {"code": self.code, "name": self.name, "description": self.description}


class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    #can't do unique bootstrap.py is adding copies of tags in this table
    # clubs = relationship("Club", secondary=tags, backref="club")

    def __init__(self, name):
        self.name = name

favorites = db.Table('user_favorites',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('club_id', db.Integer, db.ForeignKey('club.id'))
    )

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    user_name = db.Column(db.String(30), unique=False, nullable=False)

    # posts = db.relationship('Post', backref='author', lazy=True) 
    #one-to many relationship between user and posts
    #could input many-many table with user.id and club.id
    #reviews posted under user.user_name?

    def __repr__(self):
        return f"User('{self.user_name}', '{self.name}')"

    def __init__(self, name, user_name):
        self.name = name
        self.user_name = user_name
    
    def serialize(self):
        return {"name": self.name, "user_name": self.user_name}

# class Post(db.Model):
#     __tablename__ = "post"
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), unique=False, nullable=False)
#     content = db.Column(db.Text, unique=False, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


#     def __init__(self, title, content):
#        self.title = title
#        self.content = content