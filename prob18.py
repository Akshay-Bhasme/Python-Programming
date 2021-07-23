#Problem: Write a program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.

a= int(input("Enter the number"))
b= int(input("Enter the number"))
c= int(input("Enter the number"))
sum=a+b+c
if a!=b or a!=c:
    print(sum)
elif a==b==c:
    print(3*sum)
