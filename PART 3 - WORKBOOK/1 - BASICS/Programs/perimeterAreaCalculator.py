# Write a program that accepts the width and length of a rectangular space from the user and then calculates both the perimeter and area of this space.

def calc_area(width,height): 
    area = width * height
    print(f'Area of rectangle is {area}')

def calc_perim(width,height): 
    perim = (width + height) * 2
    print(f'Perimeter of the rectangle is {perim}')

width = int(input('Enter the width of the rectangle:\n'))
height =  int(input('Enter the length of the rectangle:\n'))
calc_area(width,height)
calc_perim(width,height)