from database.models import PostPhoto, db

def get_all_photo_db():
    all_photo = PostPhoto.query.all()
    return all_photo

def get_exact_photo_db(photo_id):
    photo = PostPhoto.query.filter_by(post_id=photo_id).first()
    if photo is not None:
        return f'post_id: {photo.photo_id}, photo: {photo.photo_id}'
    else:
        return 'photo not found'

def delete_exact_photo_db(photo_id):
    photo_to_delete = PostPhoto.query.filter_by(photo_id=photo_id).first()
    db.session.delete(photo_to_delete)
    db.session.commit()
    return photo_to_delete

def change_photo_db(post_id, new_text):
    post = PostPhoto.query.filter_by(photo_id=post_id).first()
    if post:
        post.text = new_text
        db.session.commit()
