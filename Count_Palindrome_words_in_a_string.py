s=input().lower().split()
#k=s[::-1]
c=0
for i in s:
    if (i[::-1]==i):
        c+=1
print(c)        