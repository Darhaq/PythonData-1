#!/usr/bin/env python3

def find_matching(L, pattern):
    matching_indices = []
    for index, string in enumerate(L):
        if pattern in string:
            matching_indices.append(index)
    return matching_indices

def main():
    pass
    # Eksempel
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))  # Output: [0, 1, 3]

if __name__ == "__main__":
    main()
