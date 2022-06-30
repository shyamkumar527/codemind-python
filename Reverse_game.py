def rev(n):
    ans=0
    while n:
        r=n%10
        ans=(ans*10)+r
        n//=10
    return ans
n=int(input())
arr=list(map(int,input().split()))
li=[]
for i in arr:
    li.append(rev(i))
for i in li:
    print(i,end=' ')