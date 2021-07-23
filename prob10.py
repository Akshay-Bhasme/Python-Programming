# Problem: Write a program that accepts an integer(n) and computes the value of n+nn+nnn. e.g. n=5, compute 5+55+555.

n= int(input("Enter a number"))
a= n
b= int('%s%s'%(n,n))
c= int('%s%s%s'%(n,n,n))

print(a+b+c)