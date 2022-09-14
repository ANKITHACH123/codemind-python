n = int(input())

x = list(map(int,input().split()))
c = 0
t = []
for i in x:
    if x.count(i)==i and i not in t:
        c+=i
        t.append(i)

if len(t)==0:
    print(-1)
else:
    print('{:.2f}'.format(c/len(t)))
