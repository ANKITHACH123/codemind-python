n=int(input())
l=list(map(int,input().split()))
p=int(input())
k=[]
for i in l:
    if i not in k and l.count(i)==p:
        k.append(i)
if(len(k)==0):
    print("-1")
else:
    print(*k)
