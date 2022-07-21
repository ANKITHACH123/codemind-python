n=int(input())
for _ in range(n):
    a=input()
    k=a[::-1]
    if(a==k):
        if len(a)%2==0:
            print("YES EVEN")
        else:
            print("YES ODD")
    else:
        print("NO")