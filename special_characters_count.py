s=input()
c=0
'''for i in s:
    if(65<=ord(i)<=90 or 97<=ord(i)<=122):
        continue
    else:
        c+=1
print(c)        
'''
d="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789"
for i in s:
    if i==' ':
        continue
    if i not in d:
        c+=1
print(c)
    