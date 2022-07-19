s=input()
b=[]
for _ in s:
    if s.count(_)==1:
        print(_)
        break
else:
    print("-1")
    