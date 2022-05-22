n=int(input())
arr=list(map(int,input().split()))
new=list()
ans=0
for i in range(n):
    c=0
    for j in range(n):
        if arr[i]==arr[j]:
            c+=1
    if c==1:
        ans=1
        new.append(arr[i])
if ans==0:
    print('-1')
else:
    print(max(new))