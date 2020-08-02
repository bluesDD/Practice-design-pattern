from abc import ABCMeta, abstractmethod


class Strategy(ABCMeta):
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
