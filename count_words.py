s=input().split()
c=0
v="AEIOUaeiou"
for i in s:
    if i[0] in v and i[len(i)-1] not in v:
        c+=1
print(c)        