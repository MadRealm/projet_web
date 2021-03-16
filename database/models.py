from database.database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # Relationship User <--> Post
    posts = db.relationship('Post', backref='authorPost', lazy='dynamic')
    comments = db.relationship('Comment', backref='authorComment', lazy='dynamic')

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


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    # Relationship Post <--> Comment
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    post = db.relationship('Post', back_populates='comments')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

