for j in range(int(input())):
    n=int(input())
    s=input()
    d={}
    ans=0
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i in s:
        if d[i]==1:
            print(i)
            ans=1
            break
    if ans==0:
        print("-1")