def prime_number(num):
    arr=[]
    for val in range(num+1):
        if val>1:
            for i in range(2,val):
                if val%i==0:
                    break
            else:
                arr.append(val)
    return arr

def prime_factor(num,arr):
    fact=[]
    j=0
    k= len(arr)
    for x in range(k):
            for i in range(len(arr)):
                if num%arr[j]==0:
                    c=num/arr[j]
                    num=c
                    fact.append(arr[j])
            j+=1

    return fact
num1= int(input('Enter 1st number'))
num2= int(input('Enter 2nd number'))
arr1=prime_number(num1)
arr2=prime_number(num2)
k= prime_factor(num1,arr1)
y=prime_factor(num2,arr2)
print(k)
print(y)
lst=[]
if len(k)>len(y):
    r=k
    k=y
    y=r
t=0
for i in range(len(k)):
    j = 0
    for ele in range(len(y)):
        a=k[t]
        b=y[j]
        if k[t]==y[j]:
            lst.append(k[t])
            y.pop(j)
            k.pop(t)
            break
        else:
            j+=1
    else:
        t+=1

print(lst)

import itertools
z= list(itertools.chain(lst,k,y))
print(z)
import math
print('LCM = ',math.prod(z))
print('HCF = ',math.prod(lst))