""""FlaskのConfigを提供"""
import os



class DevelopmentConfig:

  DEBUG = True

  SQLALCHEMY_DATABASE_URI = "sqlite:///flask.sqlite"
  SQLALCHEMY_TRACK_MODIFICATIONS = False

Config = DevelopmentConfig
