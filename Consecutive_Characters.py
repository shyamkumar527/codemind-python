s=input()
c=0
a=0
ma=1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        c+=1
        a=1
    else:
        if c>ma:
            ma=c
        c=0
if c>ma:
    ma=c
if a==1:
    print(ma+1)
else:
    print(ma)