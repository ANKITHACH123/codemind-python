a,b=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
m=[]
for i in x:
    if i not in y:
        if i not in m:
            m.append(i)
for j in y:
    if j not in x:
        if j not in m:
            m.append(j)
print(*m)