s=input()
k=input()
for i in range(len(s)):
    if k in s[i]:
        print("True")
        print(i)
        break
else:
    print("False")