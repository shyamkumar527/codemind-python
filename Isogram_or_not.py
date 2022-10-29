s=input()
d={}
ans=1
for i in s:
    if i not in d:
        d[i]=1
    else:
        ans=0
        break
if ans==1:
    print("True")
else:
    print("False")