from flask import Flask, render_template
from flask_restx import Api, Resource
from database.models import db
from comment.commentapi import comment_bp
from hashtag.hashtagapi import hashtag_bp
from photo.photoapi import photo_bp
from user.userapi import user_bp
from posts.postapi import posts_bp
from swagger.test_swagger import swagger_bp

api = Api()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///media.db'
db.init_app(app)
api.init_app(app)

@app.route('/')
def test_api():
    html_dexkan = '<h1>Test my</h1><br><input type="file">'
    return render_template('test.html')

app.register_blueprint(comment_bp)
app.register_blueprint(hashtag_bp)
app.register_blueprint(photo_bp)
app.register_blueprint(user_bp)
app.register_blueprint(posts_bp)
app.register_blueprint(swagger_bp)

# app.run()