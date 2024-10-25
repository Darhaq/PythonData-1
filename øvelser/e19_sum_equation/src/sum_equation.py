#!/usr/bin/env python3

def sum_equation(L):
    if not L:  # Check if the list is empty
        return "0 = 0"
    else:
        # Create the equation as a string and calculate the sum
        equation = " + ".join(map(str, L))  # Join the numbers with ' + '
        total = sum(L)  # Calculate the sum
        return f"{equation} = {total}"  # Return the equation with sum

def main():
    pass
    print(sum_equation([1, 5, 7]))   # Example test case
    print(sum_equation([]))           # Test case for an empty list
    print(sum_equation([10, 20, 30])) # Another test case

if __name__ == "__main__":
    main()
