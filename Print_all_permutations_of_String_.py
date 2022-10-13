from itertools import permutations 
h=input()
a=list(permutations(list(h)))
for i in a:
    print("".join(i))