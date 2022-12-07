n=int(input())
for _ in range(n):
    s=int(input())
    t=bin(s)
    c=0
    for i in t:
        if i=='1':
            c+=1
    print(c)        