n=int(input())
a,b=0,1
print(a,end=' ')
print(b,end=' ')
for i in range(n-2):
    c=a+b
    print(c,end=' ')
    a=b
    b=c