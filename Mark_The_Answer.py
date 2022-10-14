n,k=map(int,input().split())
a=list(map(int,input().split()))
c=0
d=0
for i in range(n):
    if a[i]<=k and d<2:
        c+=1
    else:
        d+=1
print(c)