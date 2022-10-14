k=int(input())
for _ in range(k):
    d=0
    n=int(input())
    a=list(map(int,input().split()))
    min=a[0]
    for i in range(len(a)):
        if(a[i]<=min):
            d+=1
            min=a[i]
    print(d)
    