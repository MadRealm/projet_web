from database.database import db


class Follow(db.Model):
    follower_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    followed_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    authenticated = db.Column(db.Boolean, default=False)
    # Relationship User <--> Post
    posts = db.relationship('Post', backref='authorPost', lazy='dynamic')
    # Relationship User <--> Post
    comments = db.relationship('Comment', backref='authorComment', lazy='dynamic')
    liked_posts = db.relationship('PostLike', foreign_keys='PostLike.user_id', backref='user', lazy='dynamic')
    followers = db.relationship('Follow', foreign_keys=[Follow.followed_id], backref="followed", lazy='dynamic')
    followed = db.relationship('Follow', foreign_keys=[Follow.follower_id], backref="follower", lazy='dynamic')


    def is_active(self):
        return True

    #Pas nécesssairement utile
    def get_id(self):
        return self.email

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False


    def is_following(self, user):
        if user.id is None:
            return False
        return self.followed.filter_by(followed_id=user.id).first() is not None

    def is_followed_by(self, user):
        if user.id is None:
            return False
        return self.followers.filter_by(follower_id=user.id).first() is not None

    def follow(self, user):
        if not self.is_following(user):
            f = Follow(follower_id=self.id, followed_id=user.id)
            db.session.add(f)

    def unfollow(self, user):
        f = self.followed.filter_by(followed_id=user.id).first()
        if f:
            db.session.delete(f)

    def like_post(self, post):
        if not self.has_liked_post(post):
            like = PostLike(user_id=self.id, post_id=post.id)
            db.session.add(like)

    def unlike_post(self, post):
        if self.has_liked_post(post):
            PostLike.query.filter_by(
                user_id=self.id,
                post_id=post.id).delete()

    def has_liked_post(self, post):
        return PostLike.query.filter(
            PostLike.user_id == self.id,
            PostLike.post_id == post.id).count() > 0

    #c'est quoi ça ???
    def __repr__(self):
        return '<User {}>'.format(self.username)




class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    image_data = db.Column(db.BLOB)
    image_size= db.Column(db.Integer)
    # Relationship User <--> Post
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # Relationship Comment <--> Post
    comments = db.relationship('Comment', back_populates='post')
    tags = db.Column(db.Text)
    # Relationship Like <--> Post
    likes = db.relationship('PostLike', backref='post', lazy='dynamic')


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    # Relationship Post <--> Comment
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    post = db.relationship('Post', back_populates='comments')
    # Relationship User <--> Comment
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class PostLike(db.Model):
    __tablename__ = 'post_like'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))