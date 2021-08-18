import uuid

import src.model.common_logs as common_logs_model
import src.model.route_aliases as route_aliases_model
from flask import jsonify


def control_auth_for_routes(bp_name):
    route_res = route_aliases_model.RouteAliasRepository().get_by_route(route_name=bp_name)
    if len(route_res) < 1:
        msg = "Route doesn't match any alias"
        add_log(bp_name, msg)
        return jsonify({"msg": msg}), 400
    route_obj = route_res[0]
    return route_obj.alias_name

def add_log(route, log_message):
    common_logs_model.CommonLogsRepository().add_log({"id": str(uuid.uuid4()), "route": route, "log_message": log_message})
