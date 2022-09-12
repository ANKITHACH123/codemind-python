l=list(map(str,input().lower()))
a=[]
for i in l:
    if i not in a and i!=" ":
        a.append(i)
a=sorted(a)
for i in a:
    print(i,end="")