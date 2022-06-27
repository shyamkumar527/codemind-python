m=int(input())
n=int(input())
for i in range(m,n+1):
    ans=0
    x=i
    while x:
        r=x%10
        if r==0 or i%r!=0:
            ans=1
            break
        x//=10
    if ans==0:
        print(i,end=' ')