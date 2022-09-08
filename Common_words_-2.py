s=input().split()
k=input().split()
c=0
for i in s:
    if i in k and k.count(i)==1 and s.count(i)==1:
        c+=1
print(c)        