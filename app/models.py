from app import db, tmdb

class User(db.Model):

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    reviews = db.relationship('Review', backref='user', lazy='dynamic')

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.name)

class Review(db.Model):

    __tablename__ = 'review'
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    rate = db.Column(db.Float)

    def __init__(self, id=None, movie_id=None, user_id=None, rating=0):
        self.movie_id = movie_id
        self.user_id = user_id
        self.rate = rating

    def __repr__(self):
        return '<Review #id: %r>' % (self.id)

    def get_movie(self):
        return tmdb.Movies(self.movie_id)