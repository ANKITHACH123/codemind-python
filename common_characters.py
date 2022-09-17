s=input().lower()
k=input().lower()
c=[]
for i in s:
    if i not in c and i in k and i!=' ':
        c.append(i)
for i in k:
    if i not in c and i in s and i!=' ':
        c.append(i)
c=sorted(c)
if(len(c)==0):
    print("-1")
for i in c:
    print(i,end='')