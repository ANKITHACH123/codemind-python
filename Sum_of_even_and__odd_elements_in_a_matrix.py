n,m=map(int,input().split())
c=0
s=0
for i in range(n):
    a=list(map(int,input().split()))
    for j in a:
        if(j%2==0):
            c=c+j
        elif(j%2!=0):
            s=s+j
print(c,s)
