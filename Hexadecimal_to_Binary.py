n=int(input())
for _ in range(n):
    s=input()
    r=bin(int(s, 16))
    t=r[2:]
    if len(t)%4==0:
        print(t)
    elif len(t)%4==1:
        print('000'+t)
    elif len(t)%4==2:
        print('00'+t)
    else:
        print('0'+t)
