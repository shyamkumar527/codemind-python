n=int(input())
arr=list(map(int,input().split()))
min=arr[0]
for i in arr:
    if i<min:
        min=i
while min>0:
    count=0
    for i in arr:
        if i%min==0:
            count+=1
    if count==n:
        print(min)
        break
    else:
        min-=1