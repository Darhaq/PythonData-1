#!/usr/bin/env python3

def reverse_dictionary(d):
    reversed_d = {}
    for english_word, finnish_words in d.items():
        for finnish_word in finnish_words:
            # Hvis det finske ord allerede er i ordbogen, tilføj det engelske ord til listen
            if finnish_word in reversed_d:
                reversed_d[finnish_word].append(english_word)
            else:
                # Hvis det finske ord ikke findes, opret en ny post med det engelske ord i en liste
                reversed_d[finnish_word] = [english_word]
    return reversed_d

def main():
    d = {'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))

if __name__ == "__main__":
    main()
