from flask import Blueprint
from database.hashtag_serv import get_exact_hashtag_db, create_post_for_hashtag

hashtag_bp = Blueprint('hashtag', __name__, url_prefix='/hashtag')

@hashtag_bp.route('/', methods=['GET'])
def get_hashtags(size: int):
    exact_hashtag = get_exact_hashtag_db()
    if exact_hashtag:
        return {'status': 1, 'message': exact_hashtag}
    return {'status': 0, 'message': 'hashtag not found'}

@hashtag_bp.route('/<string:hashatag_name>', methods=['GET'])
def get_exact_hashtag(hashtag_name: str):
    exact_hashtag = get_exact_hashtag_db()
    if exact_hashtag:
        return {'status': 1, 'message': exact_hashtag}
    return {'status': 0, 'message': 'hashtag not found'}
