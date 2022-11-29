

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from twilio.rest import Client as TwilioClient

from config import Configuration



app = Flask(__name__)
app.config.from_object(Configuration)
CORS(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)

twilio_client = TwilioClient()


from .auth import auth
app.register_blueprint(auth)

from .projects import projects
app.register_blueprint(projects)

from . import routes

