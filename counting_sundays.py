import calendar

cal = calendar.Calendar()
count = 0

for year in range(1901,2001):
    for month in range(1,13):
        test = cal.monthdays2calendar(year,month)
        if (1,6) in test[0]:
            count+=1


print(count)
