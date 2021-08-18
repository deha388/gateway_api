import argparse
import sys
from datetime import timedelta

from flask import Flask
from flask_jwt_extended import JWTManager

import config
import routes

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'NkPmhZa42snJ5bpHmB5rr7KscPHSXHg2ugXZm7VnrfEJRyhYdbwpYzqesmdGvXtetaSn7tgK7gj4c5RPVKFxmXHRBhvJamf3VJCxs6zLVucWZ8Wq2SAexgdwsxA6nwDn'
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=1)

jwt = JWTManager(app)

module = sys.modules[__name__]


def load_config(config_file="config.json"):
    config.load(config_file=config_file)


if __name__ == '__main__':
    routes.register_blueprints(app=app)
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", help="Config File (Default -> config.json)")
    args = parser.parse_args()

    if args.config:
        load_config(args.config)
    else:
        load_config()

    config_obj = config.get()
    app.run(host=config_obj.app.host, port=config_obj.app.port)
