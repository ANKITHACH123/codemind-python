s=input().split()
v="aeiou"
c=[]
for i in s:
    d=0
    for j in range(len(i)):
        if i[j] in v:
           d+=1
    c.append(d) 
print(max(c))        