s=input()
ans=100
for i in s.split():
    c=0
    for j in i:
        if j in 'aeiouAEIOU':
            c+=1
    if c<ans:
        ans=c
print(ans)