#Problem: Write a program to count the number 4 in a given list
lst=[]
r= int(input('Enter a range'))
for i in range(r):
    n= int(input('Enter the number'))
    lst.append(n)

    c = 0
    for j in lst:
        if j==4:
            c+=1
print(c)