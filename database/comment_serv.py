from database.models import PostComment

def get_exact_photo_db(commnet_id):
    comment = PostComment.query.filter_by(commnet_id=commnet_id).first()
    if comment is not None:
        return f'post_id: {comment.commnet_id}, photo: {comment.commnet_id}'
    else:
        return 'comment not found'