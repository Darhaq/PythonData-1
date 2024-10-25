#!/usr/bin/env python3

def main():
    pass
        # Iterer gennem alle mulige værdier for to terninger (1 til 6)
    for dice1 in range(1, 7):  # Første terning
        for dice2 in range(1, 7):  # Anden terning
            if dice1 + dice2 == 5:  # Tjek om summen er 5
                print( (dice1,dice2) )
                # print(f"({dice1}, {dice2})")  # Udskriv parret, hvis summen er 5

if __name__ == "__main__":
    main()
