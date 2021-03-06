import datetime as dt
from marshmallow import Schema, fields, post_load
from pprint import pprint
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from ..database import db



# 参考：https://marshmallow.readthedocs.io/en/stable/quickstart.html

class NewUser(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  first = db.Column(db.String(80))
  last = db.Column(db.String(80))

  def __repr__(self):
    return "<NewUser(name={self.first!r})>".format(self=self)

  def add_user(self, first, last):
    self.first = first
    self.last = las

class NewUserSchema(Schema):
  id = fields.Int(dump_only=True)
  first = fields.Str()
  last = fields.Str()
  formatted_name = fields.Method("format_name", dump_only=True)

  def format_name(self, newuser):
    return "{}, {}".format(newuser.last, newuser)

  @post_load
  def make_newuser(self, data, **kwargs):
    return NewUser(**data)

def must_not_be_blank(data):
  if not data:
    raise ValidationError("Data not provided")

class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.created_at = dt.datetime.now()

  def __repr__(self):
    return "<User(name={self.name!r})>".format(self=self)


class UserSchema(Schema):
  name = fields.Str()
  email = fields.Email()
  created_at = fields.DateTime()

  @post_load
  def make_user(self, data, **kwargs):
    return User(**data)


if __name__ == "__main__":
  user = User(name="Monty", email="monty@python.org")
  scheme = UserSchema()
  serialized_result = scheme.dump(user)
  pprint(serialized_result)
  
  user_data = {
      "email": "ken@yahoo.com",
      "name": "Ken",
  }
  deserialized_result = scheme.load(user_data)
  pprint(deserialized_result)
  #{'created_at': datetime.datetime(2014, 8, 11, 5, 26, 3, 869245),
  #  'email': 'ken@yahoo.com',
  #  'name': 'Ken'}
