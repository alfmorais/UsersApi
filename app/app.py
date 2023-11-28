from flask import Flask

from app.config.database import database
from app.views.main import main_bp
from app.views.users import users_bp


def create_app():
    app = Flask(__name__)

    app.config["MONGO_URI"] = "mongodb://mongo:27017/myflaskapi"
    database.init_app(app)

    app.register_blueprint(users_bp)
    app.register_blueprint(main_bp)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
