from abc import abstractmethod, ABCMeta

class Dialog:
  @abstractmethod
  def createButton(self):
    pass
  
  def render(self):
    okButton = self.createButton()
    okButton.onClick(WindowDialog())
    okButton.render()


class WindowDialog(Dialog):
  def createButton(self):
    return WindowsButton()


class Button(metaclass=ABCMeta):
  @abstractmethod
  def render(self):
    pass
  
  @abstractmethod
  def onClick(self):
    pass


class WindowsButton(Button):
  def render(self):
    return print("Window button rended")

  def onClick(self):
    return print("Window On Click")


class Application:

  def __init__(self, os):
    if os == "Windows":
      self.dialog = WindowDialog()

  def main(self):
    self.dialog.render()

if __name__ == "__main__":
  print("App started")
  app = Application("Windows")
  app.main()
