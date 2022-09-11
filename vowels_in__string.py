s=input()
v="aeiouAEIOU"
l=[]
for i in s:
    if i in v and i not in b:
        l.append(i)
print(*l)