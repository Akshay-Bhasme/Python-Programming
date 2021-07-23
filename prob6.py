#Problem: Write a program which accepts a sequence of comma-separated numbers from user and generate list and tuple.

Numbers= input('Enter some comma separated numbers: ')
list= Numbers.split(',')
tuple=tuple(list)
print('List :', list)
print('Tuple :', tuple)
