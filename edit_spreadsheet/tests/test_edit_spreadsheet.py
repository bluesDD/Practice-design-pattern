from edit_spreadsheet import __version__, edit_spreadsheet

def test_version():
    assert __version__ == '0.1.0'

user_list = [["XXXX", "YYYY", "ZZZZ"], ["1111", "2YYYY", "3ZZZZ"]]

parser = edit_spreadsheet.SudoUserParser(user_list)

def test_append_sudo_users_works_fine():
  assert parser.append_sudo_users() == [['XXXX', 'YYYY', 'ZZZZ', 'Sudo権限'], ['1111', '2YYYY', '3ZZZZ', False]]
