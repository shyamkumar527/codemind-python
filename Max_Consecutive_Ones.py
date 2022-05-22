n=int(input())
arr=list(map(int,input().split()))
c=ma=0
for i in range(n):
    if arr[i]==1:
        c+=1
    else:
        if c>ma:
            ma=c
        c=0
if c>ma:
    ma=c
print(ma)