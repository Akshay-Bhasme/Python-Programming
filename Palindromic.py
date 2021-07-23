def palindromic(num):
    lst=[]
    while num>0:
        a=num/10
        b=num//10
        c= int((a-b)*10.1)
        num=b
        lst.append(c)
    return lst

num=int(input('Enter a number: '))
k=palindromic(num)
l=0
j=1
for i in k:
    val=10**(len(k)-j)
    x=i*val
    y=l+x
    l=y
    j+=1
if l==num:
    print('Number is Palindromic')
else:
    print('Number is not Palindromic')