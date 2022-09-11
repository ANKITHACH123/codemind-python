s=input()
v="aeiou"
l=[]
for i in s:
    if i in v:
        l.append(i)
c=0
for i in v:
    if i not in l:
        c=1
        print(i,end=" ")
if(c==0):
    print("0")