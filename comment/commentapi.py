from flask import Blueprint

comment_bp = Blueprint('comment', __name__, url_prefix='/comment')

@comment_bp.route('/<int:post_id>', methods=['GET'])
def get_all_photo(post_id: int):
    pass

@comment_bp.route('/<int:post_id>/<int:comment_user_id>', methods=['POST'])
def post_comment(post_id: int):
    pass

@comment_bp.route('/<int:comment_user_id>/<int:comment_id>', methods=['PUT'])
def change_comment(comment_user_id: int, comment_id: int):
    pass

@comment_bp.route('/<int:comment_id>/<int:comment_user_id>',  methods=['DELETE'])
def delete_comment(comment_id: int, comment_user_id: int):
    pass