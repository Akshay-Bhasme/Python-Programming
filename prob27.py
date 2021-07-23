#Problem: Write a program to concatenate all elements in a list into a string and return it.

def concatenate(lst):
    kypn=''
    for i in lst:
        kypn+=str(i)
    return kypn


#Or
lst=[1,5,5,1,0,1,2]
tuple=tuple(lst)
print('%i%i%i%i%i%i%i'%tuple)

print(concatenate(lst))