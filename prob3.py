# Problem: Write a program to print current date and time

import datetime

now= datetime.datetime.now()
print('Current date and time :')
print(now.strftime('%Y-%m-%d  %H:%M:%S'))