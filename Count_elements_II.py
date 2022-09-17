n,m=map(int,input().split())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
c=[]
d=0
for i in l:
    if i not in c and i not in k and i!=' ':
        c.append(i)
for i in k:
    if i not in c and i not in l and i!=' ':
        c.append(i)
for i in c:
    d+=1
print(d)  