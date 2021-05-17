from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from  redis import StrictRedis
from flask_wtf import CSRFProtect

class Config(object):
    DEBUG = True


    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/news"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
redis_store = StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT)

