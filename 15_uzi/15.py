import datetime
for year in range(1006, 1996 + 1, 10):
    d = datetime.date(year, 1, 26)
    if d.weekday() == 0 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
        print year
