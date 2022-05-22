n=int(input())
arr=list(map(int,input().split()))
even=odd=0
for i in range(n):
    if i%2==0:
        even+=arr[i]
    else:
        odd+=arr[i]
ans=even-odd
if ans==0:
    print('YES')
else:
    print('NO')