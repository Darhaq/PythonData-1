#!/usr/bin/env python3

class Prepend(object):
    def __init__(self, start):
        """Initializer that stores the start string."""
        self.start = start

    def write(self, s):
        """Prints the string s prepended with the start string."""
        print(self.start + s)


def main():
    pass
    p = Prepend("+++ ")  # Create an instance with the start string "+++ "
    p.write("Hello")     # This will print "+++ Hello"

if __name__ == "__main__":
    main()
