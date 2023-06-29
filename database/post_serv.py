from database.models import Post, PostPhoto, PostComment, db

def get_all_posts_db():
    all_post = Post.query.all()
    return all_post

def get_all_photo_db():
    all_post_photo = PostPhoto.query.all()
    return all_post_photo

def get_exact_post_db(post_id):
    post = Post.query.filter_by(post_id=post_id).first()
    if post is not None:
        return f'post_id: {post.post_id}, post_text: {post.post_text}'
    else:
        return 'Post not found'

def delete_exact_post_db(post_id):
    post_to_delete = Post.query.filter_by(post_id=post_id).first()
    db.session.delete(post_to_delete)
    db.session.commit()
    return post_to_delete

def change_post_text_db(post_id, new_text):
    post = Post.query.filter_by(id=post_id).first()
    if post:
        post.text = new_text
        db.session.commit()

def add_comment_post_db(post_id, comment_user_id, user_id):
    new_comment = PostComment(post_id=post_id, comment_user_id=comment_user_id, user_id=user_id)
    db.session.add(new_comment)
    db.session.commit()
    return new_comment

def post_new_photo_db(user_id, photo_path):
    new_post_photo = PostPhoto(user_id=user_id, photo_path=photo_path)

    db.session.add(new_post_photo)
    db.session.commit()

    return new_post_photo.photo_id
def add_new_post_db(user_id, photo_id, post_text):
    new_post = Post(user_id=user_id, photo_id=photo_id, post_text=post_text)
    db.session.add(new_post)
    db.session.commit()
    return new_post.post_id