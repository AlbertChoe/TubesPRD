from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'bacotlu'

    from .views import views
    from .auth import auth
    from .botchat import botchats

    app.register_blueprint(botchats, url_prefix = '/')
    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')

    return app
