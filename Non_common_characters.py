s=input().lower()
k=input().lower()
u=[]
c=0
for i in s:
    if i not in k and i not in u and i!=' ':
        u.append(i)
for i in k:
    if i not in s and i not in u and i!=' ':
        u.append(i)
for i in u:
    c+=1
print(c)    