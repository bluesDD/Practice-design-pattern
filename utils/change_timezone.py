from datetime import timedelta, date

now = date.today()
print(now)
day = date.today() + timedelta(hours=-24)
some = day.strftime("%Y-%m-%d")
print(some)
day = date.today() + timedelta(hours=+24)
some = day.strftime("%Y-%m-%d")
print(some)
