n=int(input())
arr=list(map(int,input().split()))
res=list()
for i in arr:
    if i in res:
        print(i)
        break
    else:
        res.append(i)