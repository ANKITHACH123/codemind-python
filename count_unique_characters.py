s=input().lower()
b=[]
c=0
for i in s:
    if s.count(i)==1 and i!=' ':
        c+=1
if(c==0):
    print("0")
else:
    print(c)