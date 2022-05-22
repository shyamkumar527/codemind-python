n=int(input())
arr=list(map(int,input().split()))
new=list()
ans=0
for i in arr:
    if i not in new:
        count=0
        new.append(i)
        for j in range(n):
            if i==arr[j]:
                count+=1
        ans+=(count//2)
print(ans)