p=int(input())
n=bin(p)
s=n[2:]
t=str(s)
f=''
for i in t:
    if i=="1":
        f+='0'
    else:
        f+="1"
g=int(f,2)
print(g)

