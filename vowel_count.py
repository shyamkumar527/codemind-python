s=input()
ans=0
for i in s:
    if i in 'aeiouAEIOU':
        ans+=1
print(ans)