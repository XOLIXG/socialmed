from flask import Blueprint, request
from flask_restx import Resource, Api, fields
from database.user_serv import add_user_db, get_exact_user_db, get_all_users_db, delete_user_db

swagger_bp = Blueprint('swagger', __name__, url_prefix='/docs')
api = Api(swagger_bp)
model_user = api.model('registration', {'username': fields.String,
                                         'first_name': fields.String,
                                         'last_name': fields.String,
                                         'email': fields.String,
                                         'birthday': fields.Date})
user_id_field = api.model('user_id', {'user_id': fields.Integer})

@api.route('/test-user')
class TestSwagger(Resource):
    def get(self):
        all_users = get_all_users_db()
        return {'message': all_users}

@api.route('/')
class UserServ(Resource):
    @api.expect(user_id_field)
    def get(self):
        response = request.json
        user_id = response.get('user_id')
        exact_user = get_exact_user_db(user_id)

        return {'message': exact_user}

    @api.expect(user_id_field)
    def delete(self):
        response = request.json
        user_id = response.get('user_id')
        delete_user = delete_user_db(user_id)
        return {'message': delete_user}

    @api.expect(model_user)
    def post(self):
        response = request.json
        new_user = add_user_db(**response)
        print(response)
        return {'status': 'Registered'}