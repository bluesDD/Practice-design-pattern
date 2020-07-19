import datetime as dt
from marshmallow import Schema, fields
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


if __name__ == "__main__":
  user = User(name="Monty", email="monty@python.org")
  scheme = UserSchema()
  result = scheme.dump(user)
  pprint(result)
