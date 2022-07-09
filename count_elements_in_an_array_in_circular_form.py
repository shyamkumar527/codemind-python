n=int(input())
arr=list(map(int,input().split()))
b=arr
ans=0
b.append(arr[0])
b.append(arr[1])
for i in range(n):
    if (b[i]%2!=0 and b[i+2]%2==0) or (b[i]%2==0 and b[i+2]%2!=0):
        ans+=1
print(ans)