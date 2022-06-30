n=int(input())
arr=list(map(int,input().split()))
c=steps=0
for i in range(0,n-2,2):
    steps+=1
    if arr[i]<arr[i+1] and arr[i+1]>arr[i+2]:
        c+=1
if c==0 or c!=steps:
    print('-1')
else:
    print(c)