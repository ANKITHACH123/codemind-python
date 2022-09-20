n=input()
k="aeiouAEIOU"
b=[]
for i in n:
    if i in k and i not in b:
        b.append(i)
print(*b)