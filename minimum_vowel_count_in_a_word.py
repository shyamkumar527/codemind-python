s=input()
v="AEIOUaeiou"
l=s.split()
ans=1000
for i in l:
    c=0
    for j in i:
        if j in v:
            c+=1
    if c<ans:
        ans=c
print(ans)