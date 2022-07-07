n=int(input())
arr=list(map(int,input().split()))
even=[]
odd=[]
for i in range(n):
    if arr[i]%2==0:
        even.append(arr[i])
    else:
        odd.append(arr[i])
for i in odd:
    print(i,end=' ')
for i in even:
    print(i,end=' ')