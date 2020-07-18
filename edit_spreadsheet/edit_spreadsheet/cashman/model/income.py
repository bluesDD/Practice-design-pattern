from marshmallow import post_load
from .transaction import Transaction, TransactionSchema
from .transaction_type import transactionType


class Income(Transaction):
  def __init__(self, description, amount):
    super(Income, self).__init__(description, amount, transactionType.INCOME)

  def __repr__(self):
    return "<Income(name={self.description!r})>".format(self=self)

class IncomeSchema(TransactionSchema):
  @post_load
  def make_income(self, data):
    return Income(**data)
