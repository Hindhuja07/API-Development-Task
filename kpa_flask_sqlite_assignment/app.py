from flask import Flask
from dotenv import load_dotenv
from extensions import db
from routes.kpa_routes import kpa_bp

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kpa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(kpa_bp, url_prefix='/api')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
