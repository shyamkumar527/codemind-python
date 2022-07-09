s=input()
ans=0
for i in s.split():
    for j in i:
        if(j.isalpha()==0):
            ans+=1
print(ans)