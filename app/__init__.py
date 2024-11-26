from flask import Flask

def iniciar_app():
    app = Flask(__name__)
    app.config.from_object('config')

    # Registrar Blueprints
    from app.controllers.acao_controller import acao_bp
    app.register_blueprint(acao_bp)

    return app