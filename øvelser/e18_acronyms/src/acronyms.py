#!/usr/bin/env python3


import string


def acronyms(s):
    # Splitting the string into words
    words = s.split()
    
    # List to store the acronyms
    acronym_list = []
    
    # Iterate over each word in the string
    for word in words:
        # Strip punctuation from each word
        word = word.strip(string.punctuation)
        
        # Check if the word is an acronym (all uppercase and length >= 2)
        if len(word) >= 2 and word.isupper():
            acronym_list.append(word)
    
    return acronym_list


def main():
    print(acronyms("""For the purposes of the EU General Data Protection Regulation (GDPR), the controller of your personal information is International Business Machines Corporation (IBM Corp.), 1 New Orchard Road, Armonk, New York, United States, unless indicated otherwise. Where IBM Corp. or a subsidiary it controls (not established in the European Economic Area (EEA)) is required to appoint a legal representative in the EEA, the representative for all such cases is IBM United Kingdom Limited, PO Box 41, North Harbour, Portsmouth, Hampshire, United Kingdom PO6 3AU."""))


if __name__ == "__main__":
    main()
