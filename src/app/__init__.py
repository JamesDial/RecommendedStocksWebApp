import os

from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

print("=" * 55)
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)
print("=" * 55)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL', '').replace(
        'postgres://', 'postgresql://') or 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'djshkru987934uhhjeu4jw9@'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

from app.survey_questions import site

app.register_blueprint(site)

from app import routes, models