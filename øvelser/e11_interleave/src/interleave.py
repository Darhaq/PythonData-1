#!/usr/bin/env python3

def interleave(*lists):
    result = []
    # Brug zip til at kombinere elementerne fra alle lister
    for elements in zip(*lists):
        result.extend(elements)  # Brug extend til at tilføje alle elementer i result
    return result

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
