#!/usr/bin/env python3

import math

class Rational(object):
    pass
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        gcd = math.gcd(numerator, denominator)  # Reduce the fraction
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    def __str__(self):
        """Return a string representation of the rational number."""
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        """Add two rational numbers."""
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator)

    def __sub__(self, other):
        """Subtract two rational numbers."""
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator)

    def __mul__(self, other):
        """Multiply two rational numbers."""
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator)

    def __truediv__(self, other):
        """Divide two rational numbers."""
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero.")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Rational(new_numerator, new_denominator)

    def __eq__(self, other):
        """Check if two rational numbers are equal."""
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):
        """Check if one rational number is less than another."""
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __gt__(self, other):
        """Check if one rational number is greater than another."""
        return self.numerator * other.denominator > other.numerator * self.denominator


def main():
    r1 = Rational(1, 4)
    r2 = Rational(2, 3)
    
    print(r1)  # Expected output: 1/4
    print(r2)  # Expected output: 2/3
    
    print(r1 * r2)  # Expected output: 1/6 (since 1/4 * 2/3 = 1/6)
    print(r1 / r2)  # Expected output: 3/8 (since 1/4 ÷ 2/3 = 3/8)
    print(r1 + r2)  # Expected output: 11/12 (since 1/4 + 2/3 = 11/12)
    print(r1 - r2)  # Expected output: -5/12 (since 1/4 - 2/3 = -5/12)
    
    print(Rational(1, 2) == Rational(2, 4))  # Expected output: True
    print(Rational(1, 2) > Rational(2, 4))  # Expected output: False
    print(Rational(1, 2) < Rational(2, 4))  # Expected output: False

if __name__ == "__main__":
    main()
