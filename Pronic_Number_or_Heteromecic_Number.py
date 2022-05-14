n=int(input())
pro=a=1
ans=0
while pro<=n:
    pro=a*(a+1)
    a+=1
    if pro==n:
        print("YES")
        ans+=1
        break
if ans==0:
    print("NO")