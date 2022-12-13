n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
if(m>n):
    print("No")
else:
    c=0
    for i in b:
        if i in a and b.count(i)<=a.count(i):
            c+=1
    if(c>0):
        print("Yes")
    else:
        print("No")
            
            
        
    