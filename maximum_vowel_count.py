s=input()
l=s.split()
v="AEIOUaeiou"
ans=0
for i in l:
    c=0
    le=len(i)
    for j in range(le):
        if i[j] in v:
            c+=1
    if c>ans:
        ans=c
print(ans)