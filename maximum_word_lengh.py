s=input()
l=s.split()
ans=0
for i in l:
    if len(i)>ans:
        ans=len(i)
print(ans)