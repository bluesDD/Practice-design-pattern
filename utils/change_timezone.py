from datetime import timedelta, date, datetime

now = date.today()
print(now)
day = date.today() + timedelta(hours=-23)
some = day.strftime("%Y-%m-%d")
print(some)
day = date.today() + timedelta(hours=+24*8)
some = day.strftime("%Y-%m-%d")
print(some)
day = datetime.now() + timedelta(hours=+2)
some = day.strftime("%Y-%m-%d")
print(some)
