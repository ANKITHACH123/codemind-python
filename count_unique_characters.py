n=input()
p=list(n)
c=0
for i in p:
    if  i in 'abcdefghijklmnopqrstuvwxyz' and p.count(i)==1:
        c+=1
print(c)