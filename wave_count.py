n=int(input())
a=list(map(int,input().split()))
y=0
c=0
for i in range(0,n-2,2):
    if (a[i]<a[i+1]) and (a[i+1]>a[i+2]):
        y=1
        c+=1
    elif a[i]>a[i+1]:
        y=0
        break
if y==0:
    print("-1")
else:
    print(c)