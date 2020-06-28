from edit_spreadsheet import UserList

class EnvDuplicator:
  users_arrays = []

  def __init__(self, users_arrays):
    self.users_arrays = users_arrays

  def copy_status(self):
    for a in range(len(self.users_arrays)):
      user_parameters = self.users_arrays[a][2:]
      for i in range(3):
        self.users_arrays[a].extend(user_parameters)
    return self.users_arrays

with open("test_user.yml") as f:
  lines = [trimed_line.strip() for trimed_line in f.readlines()]

user_list = UserList(lines)
arrays = user_list.create_users_arrays()
e = EnvDuplicator(arrays)
print(e.copy_status())
