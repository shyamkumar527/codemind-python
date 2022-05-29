s=input()
res=list()
top=-1
flag=0
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
            flag=1
            break
if flag==0:
    print('True')
else:
    print('False')