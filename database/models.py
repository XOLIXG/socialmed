from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    reg_date = db.Column(db.DateTime)

class Paswword(db.Model):
    __tablename__ = 'user_passwords'
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    password = db.Column(db.String, nullable=False)

class PostPhoto(db.Model):
    __tablename__ = 'user_photos'
    photo_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=False)
    photo_path = db.Column(db.String, nullable=False)

    user_fk = db.relationship(User)

class Post(db.Model):
    __tablename__ = 'user_post'
    post_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=False)
    photo_id = db.Column(db.Integer, db.ForeignKey('user_photos.user_id'), primary_key=False)

    post_text = db.Column(db.String)
    post_date = db.Column(db.DateTime)

    user_fk = db.relationship(User)
    photo_fk = db.relationship(PostPhoto)

class PostComment(db.Model):
    __tablename__ = 'post_comment'
    comment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(db.Integer, db.ForeignKey('user_post.post_id'), primary_key=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=False)
    photo_id = db.Column(db.Integer, db.ForeignKey('user_photos.user_id'), primary_key=False)

    comment_text = db.Column(db.String)
    comment_date = db.Column(db.DateTime)

    user_fk = db.relationship(User)
    photo_fk = db.relationship(PostPhoto)

class Hashtag(db.Model):
    __tablename__ = 'hashtags'
    hashtag_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(db.Integer, db.ForeignKey('user_post.post_id'), primary_key=False)
    hashtag_name = db.Column(db.String, nullable=False)

    post_fk = db.relationship(Post)