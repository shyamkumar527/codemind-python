def rev(n):
    ans=0
    while n:
        r=n%10
        ans+=r
        n//=10
    return ans
n=int(input())
arr=list(map(int,input().split()))
res=0
for i in arr:
    res+=rev(i)
print(res)