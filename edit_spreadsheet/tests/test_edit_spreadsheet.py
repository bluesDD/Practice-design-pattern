from edit_spreadsheet import __version__, edit_spreadsheet
from edit_spreadsheet.cashman.index import get_newuser, app
from edit_spreadsheet.cashman.model.user import NewUser, NewUserSchema
import pytest
import json


def test_version():
    assert __version__ == '0.1.0'

user_list = [["XXXX", "YYYY", "ZZZZ"], ["1111", "2YYYY", "3ZZZZ"]]

parser = edit_spreadsheet.SudoUserParser(user_list)

def test_append_sudo_users_works_fine():
  assert parser.append_sudo_users() == [['XXXX', 'YYYY', 'ZZZZ', 'Sudo権限'], ['1111', '2YYYY', '3ZZZZ', False]]

def test_flask_api_routing():
  with app.test_client() as c:
    response = c.get("/")
    assert response.status_code == 200
    assert response.data == b'Hi guys'

    user_response = c.get("/user")
    assert user_response.status_code == 200

  with app.test_client() as c:
    newuser_response = c.get("/newuser")
    assert newuser_response.status_code == 200

    # newuser_insert_response = c.post("/newuser")
    # assert newuser_insert_response.status_code == 200

