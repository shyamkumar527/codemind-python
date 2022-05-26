n=int(input())
arr=list(map(int,input().split()))
tar=int(input())
ind=-1
for i in range(n):
    if arr[i]==tar:
        ind=i
        break
print(ind)