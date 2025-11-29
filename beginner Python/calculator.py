import math

print('Welcome to the Area Calculator!')
print('''
    ==================
    Area Calculator 📐
    ==================

        1) Triangle
        2) Rectangle
        3) Square
        4) Circle
        5) Quit
''')

shape = input('Which shape? (1-5) :     ')

if shape == '1':
    base = float(input('\nEnter the base of the triangle: '))
    height = float(input('Enter the height of the triangle: '))
    area = 0.5 * base * height
    print(f'\nThe area of the triangle is {area}')
elif shape == '2':
    length = float(input('\nEnter the length of the rectangle: '))
    width = float(input('Enter the width of the rectangle: '))
    area = length * width
    print(f'\nThe area of the rectangle is {area}')  
elif shape == '3':
    side = float(input('\nEnter the side length of the square: '))
    area = side * side
    print(f'\nThe area of the square is {area}')
elif shape == '4':
    radius = float(input('\nEnter the radius of the circle: '))
    area = math.pi * radius**2  
    print(f'\nThe area of the circle is {area}')
elif shape == '5':
    print('\nGoodbye!')


#by Georg Mueller 23.11.2025 with VCC