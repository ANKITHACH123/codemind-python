n=int(input())
for _ in range(n):
    k=input()
    l=list(k)
    l.reverse()
    c=0
    for i in range(len(l)):
        c=c+int(l[i])*(2**i)
    print(c)    
        
    