s=input().lower()
k=input().lower()
c=[]
d=[]
for i in s:
    if i not in c and i not in k and i!=' ':
        c.append(i)
for i in k:
    if i not in s and i not in c and i!=' ':
        c.append(i)
c=sorted(c)
for i in c:
    print(i,end='')