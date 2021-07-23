# Problem: Write a program to get the difference between a given number and 17, if the number is greater
# than 17 return double the absolute difference.

a=17
b= int(input('Enter a number'))
if a>b:
    c=a-b
    print(c)
else:
    c=b-a
    print(2*c)