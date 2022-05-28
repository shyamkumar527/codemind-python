s=input()
a=0
for i in range(len(s)):
    x=s.count(s[i])
    if x==1:
        a=1
        print(i)
        break
if a==0:
    print('-1')