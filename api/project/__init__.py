import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.middleware.proxy_fix import ProxyFix

db = SQLAlchemy()
cors = CORS()


def create_app(script_info=None):
    # This is a workaround for Alpine Linux (musl libc) quirk:
    # https://github.com/docker-library/python/issues/211
    import threading
    threading.stack_size(2 * 1024 * 1024)

    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)

    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    db.init_app(app)
    cors.init_app(app)

    from project.api.content import content_api
    app.register_blueprint(content_api)

    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
