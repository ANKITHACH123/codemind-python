n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
c=0
for i in a:
    if i not in b:
        c=1
for i in b:
    if i not in a:
        c=1
if(c==1):
    print("False")
else:
    print("True")
        