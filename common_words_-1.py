s1=input()
s2=input()
a=s1.lower()
b=s2.lower()
ans=0
for i in a.split():
    if i in b.split():
        ans+=1
print(ans)