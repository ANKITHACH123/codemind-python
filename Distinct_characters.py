a=input().lower()
c=[]
for i in a:
    if a.count(i)==1 and i!=' ':
        c.append(i)
c=sorted(c)
if(len(c)==0):
    print("-1")
else:
    for i in c:
        print(i,end='')
