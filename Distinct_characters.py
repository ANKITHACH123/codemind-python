s=input().lower()
b=[]
for i in s:
    if i not in b and i!=' ':
        b.append(i)
b=sorted(b)
if(len(b)==0):
    print("0")
else:
    for i in b:
        print(i,end='')