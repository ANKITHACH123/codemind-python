k=input().split()
s=k[len(k)-1]
p=min(s)
if p and p.lower() in s:
    print(p.lower())
else:
    print(p)