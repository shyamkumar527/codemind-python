n=int(input())
odd=0
arr=list(map(int,input().split()))
for i in arr:
    if i%2==1:
        odd+=1
if odd>2:
    print('NO')
else:
    print('YES')