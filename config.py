import os
from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__name__))

__DATABASE_URI__ = os.environ.get("DATABASE_URI") or \
    'sqlite:///' + os.path.join(basedir, 'default.db')

if (__DATABASE_URI__.startswith("postgres://")):
    __DATABASE_URI__ = __DATABASE_URI__.replace("postgres://", "postgresql://", 1)

class Configuration(object):

    SECRET_KEY = os.environ.get("SECRET_KEY")
    ADMIN_SECRET_KEY = os.environ.get("ADMIN_SECRET_KEY")

    SQLALCHEMY_DATABASE_URI = __DATABASE_URI__
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
    TWILIO_VERIFY_SERVICE = os.environ.get('TWILIO_VERIFY_SERVICE')
    SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY') 



