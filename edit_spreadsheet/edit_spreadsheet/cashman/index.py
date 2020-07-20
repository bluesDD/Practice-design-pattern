from flask import Flask, jsonify, request
from .model.expense import Expense, ExpenseSchema
from .model.income import Income, IncomeSchema
from .model.transaction_type import TransactionType
from .model.user import User, UserSchema
import sys


app = Flask(__name__)

transactions = [
  Income("Salary", 5000),
  Income("Dividends", 200),
  Expense("Pizza", 50),
  Expense("Pasta", 50),
  Expense("Rock Concert", 100)
]
user_data = {
    "email": "ken@yahoo.com",
    "name": "Ken",
}
@app.route('/')
def index():
  return "Hi guys"

@app.route('/incomes')
def get_incomes():
  schema = IncomeSchema(many=True)
  incomes = schema.dump(
    filter(lambda t: t.type == TransactionType.INCOME, transactions)
  )
  return jsonify(incomes)

@app.route('/incomes', methods=["POST"])
def add_income():
  income = IncomeSchema().load(request.get_json())
  transactions.append(income)
  return "", 204

@app.route('/expenses')
def get_expenses():
  schema = ExpenseSchema(many=True)
  expenses = schema.dump(
    filter(lambda t: t.type == TransactionType.EXPENSE, transactions)
  )
  return jsonify(expenses)

@app.route('/expenses', methods=["POST"])
def add_expense():
  expense = ExpenseSchema().load(request.get_json())
  transactions.append(expense)
  return "", 204

@app.route('/user')
def get_user():
  schema = UserSchema()
  user = schema.dump(user_data)
  return jsonify(user)


if __name__ == "__main__":
  app.run()
