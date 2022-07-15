s=input()
b=[]
c=0
for i in s:
    if i in s and i not in b:
        b.append(i)
if(len(s)==len(b)):
    print("True")
else:
    print("False")