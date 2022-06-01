s=input()
c=0
for i in s:
    if i=='U':
        c-=2
    if i=='D':
        c+=2
    if i=='L':
        c+=3
    if i=='R':
        c-=3
if(c==0):
    print('True')
else:
    print('False')