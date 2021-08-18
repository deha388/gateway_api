import jwtMng
import src.model.users as users
import src.utils.common as common
from flask import Blueprint, jsonify, request
from flask_jwt_extended import (create_access_token, get_jwt_identity,
                                jwt_required)

bp_name = 'api_login'

#creating Blueprint Object
api_login_bp = Blueprint(bp_name, __name__)


#login process
@api_login_bp.route('/', methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    #compare with daatabase
    user = users.UserRepository().get_by_username_and_password(username=username, password=password)
    #check if is it exist or not #### user=list
    if len(user) < 1:
        msg = "Bad username or password"
        common.add_log(bp_name, msg)
        return jsonify({"msg": msg}), 401

    #access token create for Authorization
    enc_message = jwtMng.get_encrypt_payload(user[0])
    access_token = create_access_token(identity=enc_message)
    return jsonify(access_token=access_token)

#checking URL for user ---> test process
@api_login_bp.route('/me', methods=["GET"])
@jwt_required()
def me():
    current_user = get_jwt_identity()
    dec_payload = jwtMng.get_dencrypt_payload(current_user.encode()).decode()
    return jsonify(payload=dec_payload), 200
