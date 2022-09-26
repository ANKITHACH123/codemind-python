a=input()
c=1
k= 0
for i in range(len(a)-1):
    if a[i] == a[i+1]:
        c+=1
    else:
        k=max(k,c)
        c=1
k=max(k,c)
print(k)
        