s=input()
ans=[0,0]
for i in s:
    if i=='U':
        ans[1]+=1
    elif i=='D':
        ans[1]-=1
    elif i=='L':
        ans[0]-=1
    elif i=='R':
        ans[0]+=1
if ans==[0,0]:
    print("True")
else:
    print("False")