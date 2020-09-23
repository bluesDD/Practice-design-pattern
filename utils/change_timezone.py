from datetime import datetime, timezone, timedelta

print(timezone.utc)
print(datetime.now())
tz_jst = timezone(timedelta(hours=9))
print(tz_jst)
