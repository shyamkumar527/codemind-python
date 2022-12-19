s=input()
l=[]
t=""
ans=""
c=0
v="AEIOUaeiou"
for i in s:
    if i in v:
        t+="#"
        c+=1
        l.append(i)
    else:
        t+=i
for i in t:
    if i=="#":
        ans+=l[c-1]
        c-=1
    else:
        ans+=i
print(ans)