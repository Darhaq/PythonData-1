#!/usr/bin/env python3

from linecache import getline


def word_frequencies(filename):
    """Return a dictionary with the frequency of each word in the specified file."""
    wd = {}

    # Open the file with the given filename
    with open(filename, 'r', newline="\r\n") as f:
            s = f.read()
        # Read lines from the file
        # for line in file:
            # Normalize spaces and split the line into words
            words = [w.strip("""!"#$%&'()*,-./:;?@[]_""") for w in s.split()]
            for w in words:
                if w in wd:
                      wd[w] +=1
                else:
                      wd[w] = 1

    return wd

def main():
    pass
    # Call the word_frequencies function with the filename 'alice.txt'
    fname = r'C:\Users\Tec\Desktop\PythonData-1\øvelser\e24_word_frequencies\src\alice.txt'
    wd = word_frequencies(fname)

    print(wd)

if __name__ == "__main__":
    main()
