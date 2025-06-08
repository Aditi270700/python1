# python in datetime module

# import module named datetime to work with dates as date objects.

import datetime

# it returns current date and  time
x=datetime.datetime.now()
print(x)


# The date contains year, month, day, hour, minute, second, and microsecond

# creatimg Date objects

x=datetime.datetime(2025,6,8)
print(x)


m=x.strftime("%d")
print(m)


