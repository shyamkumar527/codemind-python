s=input()
ans=res=0
for i in s.split():
    c=0
    for j in i:
        if j in 'aeiouAEIOU':
            c+=1
    if c>ans:
        ans=c
for i in s.split():
    c=0
    for j in i:
        if j in 'aeiouAEIOU':
            c+=1
    if c==ans:
        res+=1
print(res)