n=int(input())
c=[]
for i in range(2,n):
    if n%i==0:
        c.append(i)
for i in c:
    print(i,end=' ')
if(len(c)==0):
    print("-1")