n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in arr:
    if i not in l:
        l.append(i)
        x=arr.count(i)
        print(i,x,end=' ')