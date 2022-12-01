#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    nb = len(sys.argv)
    som = 0
    if nb == 1:
        print(0)
        exit()
    for i in range(1, nb):
        som += int(sys.argv[i])
    print(som)
