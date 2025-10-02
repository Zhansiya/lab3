from itertools import permutations

def string():
    s = input()
    perms = permutations(s)
    for p in perms:
        print("".join(p))

string()