from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), unique = True)
    email = db.Column(db.String(120), unique = True)
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')

    def is_authenticated(self):
        #should return true unless the object is a user that should not be allowed to 
        #authenticate for some reason
        return True

    def is_active(self):
        #should return True for users unless they are inactive (i.e. they are banned)
        return True

    def is_anonymous(self):
        #should return True only for fake users that are not supposed to log in to the system
        return False

    def get_id(self):
        #returns a unique identifer for the user in unicode format. 
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.nickname)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)
