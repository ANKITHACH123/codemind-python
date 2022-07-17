s=list(map(str,input().split()))
a=[]
for i in s:
    a.append(min(i))
    a.append(max(i))
for i in a:
    print(i,end=' ')
 