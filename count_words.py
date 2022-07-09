s=input()
ans=0
v='aeiouAEIOU'
for i in s.split():
    if i[0] in v and i[-1] not in v:
        ans+=1
print(ans)