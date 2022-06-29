n=int(input())
arr=list(map(int,input().split()))
dig=0
l=[]
for i in range(n):
    x=arr[i]
    c=0
    if x<0:
        x*=-1
    while x:
        c+=1
        x//=10
    if c>dig:
        dig=c
for i in range(n):
    c=a=0
    if arr[i]<0:
        a=1
        arr[i]*=-1
    x=arr[i]
    while x:
        c+=1
        x//=10
    if a==1:
        arr[i]*=-1
    if c==dig and arr[i] not in l:
        l.append(arr[i])
        print(arr[i],end=' ')
    if dig==1 and arr[i]==0 and arr[i] not in l:
        l.append(arr[i])
        print(arr[i],end=' ')