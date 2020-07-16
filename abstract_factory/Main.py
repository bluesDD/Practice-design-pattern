from __future__ import annotations
from abc import ABCMeta, abstractmethod

# 参考：https://refactoring.guru/design-patterns/abstract-factory
class GUIFactory(metaclass=ABCMeta):
  @abstractmethod
  def create_button(self):
    pass

  @abstractmethod
  def create_checkbox(self):
    pass


class WinFactory(GUIFactory):
  def create_button(self):
    return WinButton()

  def create_checkbox(self):
    return WinCheckbox()


class MacFactory(GUIFactory):
  def create_button(self):
    return MacButton()

  def create_checkbox(self):
    return MacCheckbox()

class Button(metaclass=ABCMeta):
  @abstractmethod
  def paint(self):
    pass

class WinButton(Button):
  def paint(self):
    return print("Win buttonpainted")

class MacButton(Button):
  def paint(self):
    return print("Mac button painted")

class Checkbox(metaclass=ABCMeta):
  @abstractmethod
  def paint(self):
    pass

class WinCheckbox(Checkbox):
  def paint(self):
    return print("Win chkbox painted")

class MacCheckbox(Checkbox):
  def paint(self):
    return print("Mac checkbox painted")


def application(factory: AbstractFactory):
  checkbox = factory.create_checkbox()
  bottun = factory.create_button()

  checkbox.paint()
  bottun.paint()


if __name__ == "__main__":
  application(WinFactory())
  application(MacFactory())
