n=int(input())
l=list(map(int,input().split()))
d=''
for i in l:
    if l.count(i)==1:
        d+=str(i)
print(d)
        