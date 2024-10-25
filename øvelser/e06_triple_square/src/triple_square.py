#!/usr/bin/env python3


def main():
    pass

def triple(x):
    return x * 3  # Funktion til at gange x med 3

def square(x):
    return x ** 2  # Funktion til at kvadrere x (x^2)

def main():
    # For loop der itererer fra 1 til 10
    for i in range(1, 11):
        t = triple(i)  # Beregn triple af i
        s = square(i)  # Beregn kvadratet af i
        # Stop loopen hvis kvadratet er større end triplet
        if s > t:
            break
        print(f"triple({i})=={t} square({i})=={s}")

if __name__ == "__main__":
    main()
