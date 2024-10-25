#!/usr/bin/env python3

import math


def main():
    # enter you solution here
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ")
        if shape == "":
            break
        if shape == 'triangle':
            b = float(input('Give base of the triangle: '))
            h = float(input('Give height of the triangle: '))
            a = 0.5 * h * b
            print(f'The area is {a:6f}')
        elif shape == 'rectangle':
            w = float(input('Give width of the rectangle: '))
            h = float(input('Give height of the rectangle: '))
            a = h * w
            print(f'The area is {a:6f}')
        elif shape == 'circle':
            r = float(input('Give radius of the circle: '))
            a = math.pi * r**2
            print(f'The area is {a:6f}')
        else:
            print('Unknown shape!')

if __name__ == "__main__":
    main()
