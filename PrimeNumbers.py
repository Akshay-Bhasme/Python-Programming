#Print all prime numbers in an interval.

def prime(start,end):
    for num in range(start,end+1):
        if num >1:
            for i in range(2,num):
                if num%i==0:
                    break
            else:
                print(num)



a= int (input('Enter the starting number'))
b= int (input('Enter the ending number'))

prime(a,b)