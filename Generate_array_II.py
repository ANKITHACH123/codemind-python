n=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(0,n,2):
    while l[i+1]:
        a.append(l[i])
        l[i+1]-=1
print(*a)        