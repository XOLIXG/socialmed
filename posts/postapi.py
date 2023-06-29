from flask import Blueprint, request
from database.post_serv import get_all_posts_db, get_exact_post_db, delete_exact_post_db, post_new_photo_db, add_new_post_db, change_post_text_db
from database.hashtag_serv import  create_post_for_hashtag

posts_bp = Blueprint('user_post', __name__, url_prefix='/post')

@posts_bp.route('/add_post', methods=['POST'])
def add_post(post_text: str, user_id: int):
    file = request.files.get('post_photo', '')
    file.save(f'user_images/{file.filename}')

    hashtags = request.json.get('hashtags')

    new_photo_id = post_new_photo_db(user_id, file.filename)

    new_post_id = add_new_post_db(user_id, photo_id=new_photo_id, post_text=post_text)

    if hashtags:
        create_post_for_hashtag(new_post_id, hashtags)

    return {'status': 1, 'message': 'Post added'}
@posts_bp.route('/', methods=['GET'])
def get_all_posts():
    all_post = get_all_posts()
    return all_post

@posts_bp.route('/<int:post_id>', methods=['GET'])
def get_exact_post(post_id: int):
    exact_photo = get_exact_post_db()
    if exact_photo:
        return {'status': 1, 'message': exact_photo}
    return {'status': 0, 'message': 'User not found'}

@posts_bp.route('/<int:user_id>/<int:post_id>', methods=['PUT'])
def change_post(post_id: int):
    new_post_text = request.json.get('new_post_text')

    change_post_text_db(post_id, new_post_text)

    return {'tstatus': 1, 'message': 'post change successfuly'}

@posts_bp.route('/<int:user_id>/<int:post_id>',  methods=['DELETE'])
def delete_post(post_id: int):
    delete_post = delete_exact_post_db()
    if delete_post:
        return {'status': 1, 'message': 'photo deleted'}
    return {'status': 0, 'message': 'photo not found'}