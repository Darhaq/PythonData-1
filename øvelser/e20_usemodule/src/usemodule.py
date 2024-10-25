#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():
    # Call the functions from triangle module
    a = 3
    b = 4
    
    hypo = triangle.hypothenuse(a, b)
    area = triangle.area(a, b)
    
    print(f"The hypothenuse of the triangle with sides {a} and {b} is {hypo}")
    print(f"The area of the triangle with sides {a} and {b} is {area}")

if __name__ == "__main__":
    main()
