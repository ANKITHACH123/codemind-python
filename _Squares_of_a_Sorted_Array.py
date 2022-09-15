n=int(input())
k=[]
l=list(map(int,input().split()))
for i in l:
    k.append(i*i)
k=sorted(k)
print(*k)