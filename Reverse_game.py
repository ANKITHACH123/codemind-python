def rev(n):
    rev=0
    while n:
        r=n%10
        n//=10
        rev=rev*10+r
    return rev
n=int(input())
l=list(map(int,input().split()))
for i in l:
    print(rev(i),end=' ')