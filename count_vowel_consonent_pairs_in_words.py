s=input()
m=s.split()
ans=0
for j in m:
    le=len(j)
    x=len(j)-1
    v="AEIOUaeiou"
    c="BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    for i in range(le//2):
        if j[i] in v and j[x] in c:
            ans+=1
        elif j[i] in c and j[x] in v:
            ans+=1
        x-=1
print(ans)