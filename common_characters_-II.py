s=input().lower()
k=input().lower()
c=0
t=[]
for i in s:
    if i in k and i not in t and i!=' ':
        t.append(i)
for i in k:
    if i in s and i not in t and i!=' ':
        t.append(i)
for i in t:
    c+=1
print(c)    