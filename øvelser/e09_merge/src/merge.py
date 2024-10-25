#!/usr/bin/env python3
def merge(L1, L2):
    pass
    L = []
    i1 = 0
    i2 = 0
    while (i1 < len(L1) and i2 < len(L2)):
        if L1[i1] < L2[i2]:
            L.append(L1[i1])
            i1 += 1
        else:
            L.append(L2[i2])
            i2 += 1

    L += L1[i1:] + L2[i2:]
    return L

def main():
    pass
    l1 = [2,4,5,9, 100]
    l2 = sorted([7,9,4,8,4])
    print(merge(l1, l2))

if __name__ == "__main__":
    main()
