s=input().lower()
s=list(s)
b=[]
for i in s:
    if s.count(i)==1:
        b.append(i)
for i in b:
    print(i)
    break
if(len(b)==0):
    print("-1")