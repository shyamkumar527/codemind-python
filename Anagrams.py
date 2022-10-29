s1=input()
s2=input()
ans=1
for i in s1.lower():
    if i not in s2.lower():
        ans=0
        break
if ans==1:
    for i in s2.lower():
        if i not in s1.lower():
            ans=0
            break
if(ans==1):
    print("True")
else:
    print("False")