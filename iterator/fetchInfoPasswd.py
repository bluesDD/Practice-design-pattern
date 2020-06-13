class FetchInfoPasswd:
  def __init__(self, row):
    self.__row = row

  def fetchUserName(self):
    return self.__row.split(":")[0]

  def fetchUID(self):
    return self.__row.split(":")[2]

  def fetchLoginStatus(self):
    isLogin = self.__row.split(":")[6].replace("\n", "")
    if isLogin == "/sbin/nologin":
      return 1
    else:
      return 2

  def fetchPasswd(self):
    return self.fetchUID() + "," + self.fetchUserName() + "," + str(self.fetchLoginStatus())
