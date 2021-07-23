#Problem: Write a program that will accept base and height of a traingle and compute the area.

def area(base,height):
    c= (1/2)*(base*height)

    print(c)

base= int(input('Enter the base of the traingle in mm: '))
height= int(input('Enter the height of the triangle in mm: '))
area(base,height)
