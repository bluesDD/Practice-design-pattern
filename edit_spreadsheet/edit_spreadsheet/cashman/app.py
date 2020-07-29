"""flask appの初期化"""
from flask import Flask
from .database import init_db, db
from .config import Config


def create_app():
  app = Flask(__name__)
  app.config.from_object(Config)

  init_db(app)

  return app

app = create_app()
