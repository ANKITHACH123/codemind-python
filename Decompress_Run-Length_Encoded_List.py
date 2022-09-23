n=int(input())
l=list(map(int,input().split()))
for i in range(0,n,2):
    k=l[i]
    p=l[i+1]
    for j in range(k):
        print(p,end=' ')