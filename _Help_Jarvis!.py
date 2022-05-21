n=int(input())
for i in range(n):
    x=int(input())
    c=0
    ans=0
    arr=list()
    while x:
        r=x%10
        arr.append(r)
        x=x//10
        c+=1
    val=min(arr)
    for j in range(c-1):
        val+=1
        if val not in arr:
            ans=1
            break
    if ans==0:
        print('YES')
    else:
        print('NO')