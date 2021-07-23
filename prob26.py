#Problem: Write a program to create a histogram from a given list of integers.

def histogram(lst):
    for i in lst:
        a=char * i
        print(a)

char= input("Enter a char to make histogram: ")
lst=[1,2,3,4]
histogram(lst)