from flask import Flask

from app.db.database import init_db
from app.routes.menu_route import menu_blueprint

app = Flask(__name__)

if __name__ == '__main__':
    init_db()
    app.register_blueprint(menu_blueprint, url_prefix="/api/menu")
    app.run()