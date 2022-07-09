s=input()
c=input()
ans=0
for i in range(len(s)):
    if s[i]==c:
        ans=1
        print('True')
        print(i)
        break
if ans==0:
    print('False')