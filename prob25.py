#Problem: Write a program to check whether a specified value is contained in a group of values.

def available(lst):
    for j in lst:
        if find == j:
            return True
    return False

r= int(input('Enter the range: '))
lst=[]
for i in range(r):
    num= int(input('Enter a number: '))
    lst.append(num)

find=int(input('Enter the number to find: '))

k=available(lst)
print(k)
