s=input().split()
v="aeiou"
c=0
for i in s:
    c=0
    for j in range(len(i)):
        if i[j] in v:
            c+=1
    print(c,end=" ")        