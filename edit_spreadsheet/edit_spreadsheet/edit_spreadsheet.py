import csv

class UserList:
  users_arrays = [["UID", "ユーザー名", "ログイン可否"]]
  def __init__(self, lines):
    self.lines = lines

  def __create_user_data_array(self):
    index = 0
    for line in self.lines:
      if "- name:" in line:
        end = index + 7
        row_list = self.lines[index:end]
        self.__set_user_exists_flag(row_list)
        self.__remove_word("- name: ", row_list, 0)
        self.__remove_word("uid: ", row_list, 1)
        self.__change_items_order(row_list, 0, 1)
        self.__change_items_order(row_list, 2, 6)
        user_data_list = row_list[0:3]
        self.users_arrays.append(user_data_list)
      index +=  1
    return self.users_arrays

  def __change_items_order(self, array, index_a, index_b):
    array[index_a], array[index_b] = array[index_b], array[index_a]

  def __is_user_removed(self, state):
    if state in 'state: absent ':
      return True
    else:
      return False

  def __set_user_exists_flag(self, array):
    if self.__is_user_removed(array[6]):
      array[6] = 0
    else:
      array[6] = 1

  def __remove_word(self, word, array, index):
    array[index] = array[index].replace(word, "")

  def create_users_arrays(self):
    user_array = self.__create_user_data_array()
    return user_array

class SudoUserParser(UserList):
  sudo_users = ["Sudo権限", "Alice", "John"]
  permission_flag = True
  no_permission_flag = False

  def __init__(self, userlist):
    self.userlist = userlist

  def append_sudo_users(self):
    index = 0

    self.userlist[0].append(self.sudo_users[0])

    for item in self.userlist:
      if index == 0:
        pass
      elif item[1] in self.sudo_users:
        self.userlist[index].append(self.permission_flag)
      else:
        self.userlist[index].append(self.no_permission_flag)
      index += 1
    return self.userlist

class CsvWriter:
  def __init__(self, file):
    self.file = file

#  def to_csv()


if __name__ == "__main__":
    with open("test_user.yml") as f:
      lines = [trimed_line.strip() for trimed_line in f.readlines()]

    user_list = UserList(lines)
    arrays = user_list.create_users_arrays()

    s = SudoUserParser(arrays)

    with open("tmp.csv", "w") as f:
      writer = csv.writer(f)
      writer.writerows(s.append_sudo_users())
