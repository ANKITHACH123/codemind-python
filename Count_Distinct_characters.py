s=input().lower()
c=0
b=[]
for i in s:
    if i not in b and i!=' ':
        b.append(i)
        c+=1
print(c)        