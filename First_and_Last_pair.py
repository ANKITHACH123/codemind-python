k=int(input())
a=list(map(int,input().split()))
i=0
c=[]
while i!=k//2:
    c.append(a[i])
    c.append(a[(k-1)-i])
    i+=1
if len(a)%2!=0:
    c.append(a[i])
    c.append(0)
print(*c)