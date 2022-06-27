n=int(input())
l=[]
c=0
while n:
    r=n%10
    l.append(r)
    n//=10
    c+=1
for i in range(c-1,-1,-1):
    if l[i]==6:
        l[i]=9
        break
ans=0
for i in range(c-1,-1,-1):
    ans=(ans*10)+l[i]
print(ans)