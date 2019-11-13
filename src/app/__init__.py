from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from src.services.userservice import UserService
from src.database.databaseservice import DatabaseService
from src.utils.phonenumber_utils import is_valid_br_phone_number, get_e164_phone_number_from_br_number
from flask_expects_json import expects_json
from bson.json_util import dumps


app = Flask(__name__)
CORS(app)
app.config.from_object('src.app.config.Config')

db = DatabaseService()
user_service = UserService(database_service=db)



@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/users', methods=['GET'])
def list_users():
    users = list(user_service.get_users())

    return jsonify({
        'users': dumps(users),
    }), 200

insert_user_schema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'phone_number': {'type': 'string'},
        'assets': {'type': 'array'},
    },
    'required': ['phone_number', 'assets'],
}

@app.route('/users/insert', methods=['POST'])
@expects_json(insert_user_schema)
def insert_user():
    content = request.json

    phone_number = content.get('phone_number')
    if not is_valid_br_phone_number(phone_number):
        return jsonify({
            "status": "invalid phone number",
        }), 400

    user_data = {
        'assets': content.get('assets'),
        'phone_number': get_e164_phone_number_from_br_number(phone_number),
    }

    if content.get('name'):
        user_data.update({'name': content.get('name')})

    user_service.insert_user(user_data)

    return jsonify({
        "status": "phone number {} inserted".format(phone_number)
    }), 201

delete_user_with_phone_number_schema = {
    'type': 'object',
    'properties': {
        'phone_number': {'type': 'string'},
    },
    'required': ['phone_number'],
}

@app.route('/users/delete', methods=['DELETE'])
@expects_json(delete_user_with_phone_number_schema)
def delete_user_with_phone_number():
    content = request.json

    phone_number = content.get('phone_number')

    if not is_valid_br_phone_number(phone_number):
        return jsonify({
            "status": "invalid phone number",
        }), 400

    e164_phone_number = get_e164_phone_number_from_br_number(phone_number)
    user_service.delete_users_with_phone_number(e164_phone_number)

    return jsonify({
        "status": "user with phone number {} deleted".format(phone_number)
    }), 204
