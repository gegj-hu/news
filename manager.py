from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from  redis import StrictRedis
from flask_wtf import CSRFProtect
from flask_session import Session


class Config(object):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/news"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    SESSION_TYPE = "redis"  # 指定 session 保存到 redis 中
    SESSION_USE_SIGNER = True  # 让 cookie 中的 session_id 被加密签名处理
    #制定session的存储方式
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # 使用 redis 的实例
    PERMANENT_SESSION_LIFETIME = 86400  # session 的有效期，单位是秒

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
#基本配置存储方式
redis_store = StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT)
CSRFProtect(app)
Session(app)