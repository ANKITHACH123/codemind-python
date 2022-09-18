t=int(input())
for i in range(t):
    d=0
    n=int(input())
    l=list(map(int,input().split()))
    for i in range(0,len(l)):
        if l[i]%2!=0:
            d+=1
    print(d//2)        