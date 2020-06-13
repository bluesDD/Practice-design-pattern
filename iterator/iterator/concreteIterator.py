from Iterator.Iterator import Iterator

class BookShelfIterator(Iterator):
  def __init__(self, bookShelf):
    self.__bookshelf = bookShelf
    self.__index = 0

  def hasNext(self):
    return True if self.__index < self.__bookshelf.getLength() else False

  def next(self):
    book = self.__bookshelf.getBookAt(self.__index)
    self.__index += 1
    return book
