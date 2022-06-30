n=int(input())
arr=list(map(int,input().split()))
l=r=0
for i in range(n//2):
    l+=arr[i]
for i in range(n//2,n):
    r+=arr[i]
print(l)
print(r)