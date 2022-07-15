s=input()
a=[]
f=[]
for i in s.split():
    a.append(i)
for i in a:
    f.append(len(i))
print(max(f))