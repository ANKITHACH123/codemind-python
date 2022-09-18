n=int(input())
c=0
d=2
for i in range(n):
    temp=c
    c=d
    d+=temp
print(c)    