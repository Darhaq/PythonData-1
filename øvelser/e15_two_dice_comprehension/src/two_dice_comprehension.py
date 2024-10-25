#!/usr/bin/env python3

def main():
    pass
        # Listekomprehension for at finde alle par af terningekast, hvor summen er 5
    pairs = [(i, j) for i in range(1, 7) for j in range(1, 7) if i + j == 5]
    
    # Udskriv hvert par på en ny linje
    for pair in pairs:
        print(pair)

if __name__ == "__main__":
    main()
