import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type = str,
        required = True,
        help = 'This is required'
    )
    parser.add_argument('password',
        type = str,
        required = True,
        help = 'This is required'
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': "User already exist"}, 400

        new_user = UserModel(**data)
        new_user.save_to_db()

        return {'message': "User created successfully."}, 201
