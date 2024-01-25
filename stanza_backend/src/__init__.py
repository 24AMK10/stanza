from flask import Flask
from flask_assets import Environment

def init_app():
    app = Flask(__name__)

    assets = Environment()
    assets.init_app(app)
    with app.app_context():
            
        from .views.pg_search import pg_search
        from .views.appointment import appoint

        app.register_blueprint(pg_search, url_prefix='/search-pg')
        app.register_blueprint(appoint, url_prefix='/appoint')

        return app