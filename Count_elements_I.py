n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a=set(a)
b=set(b)
s=0
k=0
for i in a:
    if i in b:
        s+=1
print(s)        
        