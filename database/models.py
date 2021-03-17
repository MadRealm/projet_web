from database.database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    authenticated = db.Column(db.Boolean, default=False)
    # Relationship User <--> Post
    posts = db.relationship('Post', backref='authorPost', lazy='dynamic')
    liked_posts = db.relationship('Post', back_populates='likers_id')
    comments = db.relationship('Comment', backref='authorComment', lazy='dynamic')

    def is_active(self):
        return True

    #Pas nécesssairement utile
    def get_id(self):
        return self.email

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False

    #c'est quoi ça ???
    def __repr__(self):
        return '<User {}>'.format(self.username)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    content = db.Column(db.Text)
    image_data = db.Column(db.BLOB)
    # Relationship User <--> Post
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comments = db.relationship('Comment', back_populates='post')
    tags = db.Column(db.Text)
    likers_id = db.relationship('User', back_populates='liked_posts')
    likes = db.Column(db.Integer)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    # Relationship Post <--> Comment
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    post = db.relationship('Post', back_populates='comments')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

