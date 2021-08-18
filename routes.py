from src.controller.api.login import api_login_bp
from src.controller.api.clients import api_client_bp
from src.controller.api.ocr_trigger import api_ocr_trigger_bp


def register_blueprints(app):
    # route for API with blueprint, because of parsing smaller re-usable components
    app.register_blueprint(api_login_bp, url_prefix="/login")
    app.register_blueprint(api_client_bp, url_prefix="/api/clients")
    app.register_blueprint(api_ocr_trigger_bp, url_prefix="/api/ocr/trigger")
    #app.register_blueprint(api_rasa_trigger, url_prefix="/api/rasa/trigger")
