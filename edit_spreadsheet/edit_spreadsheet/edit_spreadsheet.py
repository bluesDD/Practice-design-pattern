with open("test_user.yml") as f:
  lines = [trimed_line.strip() for trimed_line in  f.readlines()]

class UserList:
  users_arrays = []
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

  def main(self):
    user_array = self.__create_user_data_array()
    print(user_array)

user_list = UserList(lines)
user_list.main()
