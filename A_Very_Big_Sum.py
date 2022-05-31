n=int(input())
c=0
a=list(map(int,input().split()))
for i in range(len(a)):
    c+=a[i]
print(c)    