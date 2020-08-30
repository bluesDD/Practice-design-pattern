from collections import defaultdict
from datetime import datetime

datetime.now()
# names = ["socrates", "archimedes", "plato"]

# names.sort(key=len)

# print(names)

def log_missing():
  print("Key added")
  return 0

current = {"green": 12, "blue": 3}
increments = [
  ("red", 5),
  ("blue", 17),
  ("orange", 9),
]
result = defaultdict(log_missing, current)
print("Before:", dict(result))
for key, amount in increments:
  result[key] += amount
print("After:", dict(result))
