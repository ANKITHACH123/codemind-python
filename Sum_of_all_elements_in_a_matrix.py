n,m=map(int,input().split())
c=0
for i in range(n):
    a=list(map(int,input().split()))
    for j in a:
        c=c+j
print(c)        