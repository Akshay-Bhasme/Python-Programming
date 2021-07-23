#Problem: Write a program to calculate number of days between two dates.

from datetime import date
f_date= date(2014,7,2)
l_date= date(2014,8,11)
delta= l_date - f_date
print(delta.days)