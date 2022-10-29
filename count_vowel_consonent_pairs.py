s=input()
le=len(s)
x=len(s)-1
v="AEIOUaeiou"
c="BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
ans=0
for i in range(le//2):
    if s[i] in v and s[x] in c:
        ans+=1
    elif s[i] in c and s[x] in v:
        ans+=1
    x-=1
print(ans)