s=input().split()
l=[]
b=[]
k=0
p=0
for i in s:
    l.append(min(i))
for i in s:
    b.append(max(i))
for i in l:
    k+=ord(i)
for i in b:
    p+=ord(i)
print(abs(p-k))    