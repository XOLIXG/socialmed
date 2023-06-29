from database.models import Hashtag, db

def get_exact_hashtag_db(hashag_id):
    hashtag = Hashtag.query.filter_by(hashag_id=hashag_id).first()
    if hashtag is not None:
        return f'hashtag_id: {hashtag.hashag_id}, hashtag: {hashtag.hashag_id}'
    else:
        return 'hashtag not found'

def create_post_for_hashtag(post_id, hashtags):
    created_hashtags = []
    for hashtag_name in hashtags:
        new_hashtag_post = Hashtag(post_id, hastag_name=hashtags)
        created_hashtags.append(new_hashtag_post)
    db.session.add_all(created_hashtags)
    db.session.commit()

    return True