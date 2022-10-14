a=int(input())
arr=list(map(int,input().split()))
arr2=list(map(int,input().split()))
c=0
d=0
s=0
for i in arr:
    if i==-1:
        c+=1
    else:
        d+=i
for i in arr2:
    if i==-1:
        c+=1
    else:
        s+=i
if c==2:
    print("Infinite")
else:
    e=0
    for i in range(1000):
        if i+d==s:
            e+=1
    print(e)