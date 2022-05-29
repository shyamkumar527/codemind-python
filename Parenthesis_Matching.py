s=input()
res=list()
top=-1
ans=flag=0
for i in range(len(s)):
    if s[i]=='{' or s[i]=='[' or s[i]=='(':
        top+=1
        res.append(s[i])
    else:
        if s[i]=='}' and top!=-1 and res[top]=='{':
            top-=1
            res.pop()
        elif s[i]==']' and top!=-1 and res[top]=='[':
            top-=1
            res.pop()
        elif s[i]==')' and top!=-1 and res[top]=='(':
            top-=1
            res.pop()
        else:
            ans=i+1
            flag=1
            break
if flag==0 and top!=-1:
    ans=i+2
print(ans)           