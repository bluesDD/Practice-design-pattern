import datetime as dt
from marshmallow import Schema, fields, post_load
from pprint import pprint

# 参考：https://marshmallow.readthedocs.io/en/stable/quickstart.html

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
