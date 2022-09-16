n=int(input())
for i in range(n):
    k=int(input())
    l=list(map(int,input().split()))
    if(l==sorted(l)):
        print("0")
    else:
        k=sorted(l)
        print(max(k)-min(k))
            