from app import db

class Team(db.Model):
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    captain = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    def __init__(self, name=None, captain=None):
        self.name = name
        self.captain = captain
    
    def __repr__(self):
        return '<Team %r>' % (self.name)
