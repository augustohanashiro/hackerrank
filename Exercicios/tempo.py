from datetime import datetime, timedelta
import pytz


i = int(input())
for _ in range(i):

    h1 = datetime.strptime(input(), "%a %d %b %Y %H:%M:%S %z")
    h2 = datetime.strptime(input(), "%a %d %b %Y %H:%M:%S %z")
    print("{:.0f}".format(abs(h1-h2).total_seconds()))


