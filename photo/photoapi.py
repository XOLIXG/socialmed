from flask import Blueprint, request
from database.photo_serv import get_all_photo_db, get_exact_photo_db, delete_exact_photo_db, change_photo_db
from database.post_serv import post_new_photo_db

photo_bp = Blueprint('photo', __name__, url_prefix='/photo')

@photo_bp.route('/', methods=['GET'])
def get_all_photo():
    all_photo = get_all_photo_db()
    return {'status': 1, 'message': all_photo}

@photo_bp.route('/', methods=['POST'])
def save_user_photo(user_id: int):
    file = request.files.get('image', '')
    file.save('user_images/' + file.filename)
    new_photo = post_new_photo_db(user_id, file.filename)
    return {'status': 1, 'message': 'Photo added'}


@photo_bp.route('/<int:photo_id>', methods=['POST'])
def get_exact_photo(photo_id: int):
    exact_photo = get_exact_photo_db(photo_id)
    if exact_photo:
        return {'status': 1, 'message': exact_photo}
    return {'status': 0, 'message': 'User not found'}
y

@photo_bp.route('/<int:user_id>/<int:photo_id>',  methods=['DELETE'])
def delete_photo(user_id: int, photo_id: int):
    delete_user = delete_exact_photo_db(photo_id)
    if delete_user:
        return {'status': 1, 'message': 'photo deleted'}
    return {'status': 0, 'message': 'photo not found'}