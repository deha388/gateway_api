import uuid

import jwtMng
import src.model.aliases as alias_model
import src.model.user_request_logs as userrequestlogs_model
import src.model.users as user_model
import src.utils.common as common
import src.utils.providers.alias_factory as alias_factory
from flask import Blueprint, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required

bp_name = 'api_clients'
api_client_bp = Blueprint(bp_name, __name__)


@api_client_bp.route('/', methods=["GET"])
@jwt_required()
def index():
    current_user = get_jwt_identity()
    dec_payload = jwtMng.get_dencrypt_payload(current_user.encode()).decode()

    user_res = user_model.UserRepository().get_by_username(dec_payload)
    if len(user_res) < 1:
        msg = "User not exists"
        common.add_log(bp_name, msg)
        return jsonify({"msg": msg}), 400

    # get alias
    #user_res=list , index[0] gives us current user
    user_obj = user_res[0]
    #Column alias in user_obj gives us ocr_test
    alias_name = user_obj.alias
    #if alias_name is exist,that will be match up
    alias_res = alias_model.AliasRepository().get_by_name(alias_name)

    if len(alias_res) < 1:
        msg = "User doesn't match any alias"
        common.add_log(bp_name, msg)
        return jsonify({"msg": msg}), 400

    # alias authorization check
    if alias_name != common.control_auth_for_routes(bp_name):
        msg = "User doesn't authorize to use this endpoint"
        common.add_log(bp_name, msg)
        return  jsonify({"msg": msg}), 403

    alias_obj = alias_res[0]

    #add log table, logging process
    id_ = str(uuid.uuid4())
    log = {"id": id_, "username": dec_payload, "alias_name": alias_name}
    userrequestlogs_model.UserRequestLogsRepository().add_log(log)

    #call alias_factory
    clients_res = alias_factory.get(alias_obj).get_customers()
    userrequestlogs_model.UserRequestLogsRepository().update_status(log, 200)
    return jsonify(data=clients_res), 200
