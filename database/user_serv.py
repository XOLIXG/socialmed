from database.models import User, Paswword, db


def add_user_db(email, **user_data):
    checker = check_user_db(email)
    if checker:
        return checker
    new_user = User(**user_data)
    db.session.add(new_user)
    db.session.commit()
    return new_user
def check_user_db(email):
    checker = User.query.filter_by(email=email)
    if checker:
        return checker.id
    return False

def check_user_password_db(email, password):
    checker = User.query.filter_by(email=email, password=password)
    if checker:
        return checker.id
    return False

def get_all_users_db():
    all_users = User.query.all()
    return all_users

def get_exact_user_db(user_id):
    user = User.query.filter_by(user_id=user_id).first()
    if user is not None:
        return f'Username: {user.user_id}, Email: {user.email}'
    else:
        return 'User not found'

def delete_user_db(user_id):
    user_to_delete = User.query.filter_by(user_id=user_id).first()
    if user_to_delete:
        db.session.delete(user_to_delete)
        db.session.commit()
        return True
    return False