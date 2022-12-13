n=int(input())
l=list(map(int,input().split()))
d=[]
for i in l:
    if l.count(i)!=2:
        d.append(i)
d.sort()        
print(*d)        