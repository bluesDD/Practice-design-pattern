class SimpleGradebook:
    def __init__(self):
      self._grades = {}

    def add_student(self, name):
      self._grades[name] = []

    def report_grade(self, name, score):
      self._grades[name].append(score)

    def average_grade(self, name):
      grades = self._grades[name]
      return sum(grades) / len(grades)

if __name__ == "__main__":
  book = SimpleGradebook()
  book.add_student("Isaac Newton")
  book.report_grade("Isaac Newton", 90)
  book.report_grade("Isaac Newton", 100)
  book.report_grade("Isaac Newton", 30)

  print(book.average_grade("Isaac Newton"))
