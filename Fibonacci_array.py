n=int(input())
f=list(map(int,input().split()))
c=0
y=0
for i in range(len(f)-2):
    if(f[i]+f[i+1]==f[i+2]):
        y=1
        c+=1
    else:
        y=0
        break
if(y==0):
    print("no")
else:
    print("yes")