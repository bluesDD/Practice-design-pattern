import datetime as dt
from marshmallow import Schema, fields

class Transaction():
  def __init__(self, description, amount, type):
    self.description = description
    self.amount = amount
    self.created_at = dt.datetime.now()
    self.type = type

  def __repr__(self):
    return "<Transaction(name={self.description!r})>".format(self=self)


class TransactionSchema(Schema):
  description = fileds.Str()
  amount = fileds.Number()
  created_at = fileds.Date()
  type = fileds.Str()
