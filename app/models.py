from app import db

TeamUser= db.Table('TeamUser', 
                   db.Column('id', db.Integer, primary_key=True),
                   db.Column('teamId', db.Integer, db.ForeignKey('team.id')),
                   db.Column('userId', db.Integer, db.ForeignKey('user.id')))

class Team(db.Model):
    __tablename__ = 'team'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    members = db.relationship('User', secondary=TeamUser, backref='User')

    def __init__(self, name=None, captain=None):
        self.name = name

    def __repr__(self):
        return '<Team %r>' % (self.name)

class User(db.Model):

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    teams = db.relationship('Team', secondary=TeamUser, backref='Team')

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.name)