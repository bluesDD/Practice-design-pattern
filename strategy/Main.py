from abc import ABCMeta, abstractmethod


class Strategy(metaclass=ABCMeta):
  @abstractmethod
  def execute(self, a: int, b: int) -> int:
    pass

class ConcreteStarategyAdd(Strategy):
  def execute(self, a, b):
    return a + b

class ConcreteStarategySubstract(Strategy):
  def execute(self, a, b):
    return a - b

class ConcreteStarategyMultiply(Strategy):
  def execute(self, a, b):
    return a * b


class Context:
  __strategy: Strategy

  def setStrategy(self, strategy: Strategy):
    self.__strategy = strategy

  def executeStrategy(self, a: int, b: int):
    return self.__strategy.execute(a, b)


def main():
  user_input = input("Enter your application name(add/sub/multiply): ")
  user_input_int_1 = input("Enter your first number: ")
  user_input_int_2 = input("Enter your second number: ")

  context = Context()

  if user_input == "add" :
    add = ConcreteStarategyAdd()
    context.setStrategy(add)
  elif user_input == "sub":
    sub = ConcreteStarategySubstract()
    context.setStrategy(sub)
  else:
    multi = ConcreteStarategyMultiply()
    context.setStrategy(multi)

  result = context.executeStrategy(int(user_input_int_1), int(user_input_int_2))

  print("result is: " + str(result))


if __name__ == "__main__":
  main()
