n=int(input())
a=list(map(int,input().split()))
s=len(a)
o=0;e=0
res=0
for i in range(0,s):
    if i%2!=0:
        o=o+a[i]
for i in range(0,s):
    if i%2==0:
        e=e+a[i]
res=abs(o-e)
if res==0:
    print("YES")
else:
    print("NO")     