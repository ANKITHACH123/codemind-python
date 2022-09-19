l=list(map(str,input().split()))
d=[]
for i in l:
    c=0
    for j in i:
        if j in "aeiouAEOIU":
            c+=1
    d.append(c)    
k=[]
for i in d:
    if i==min(d):
        k.append(i)
print(len(k))        