for i in range(int(input())):
    n,d,p,q=map(int,input().split())
    l=[]
    while(n):
        if n<=0:
            break
        if n-d>=0:
            l.append(d)
        else:
            l.append(n)
        n-=d
    ans=0
    c=1
    for i in l:
        ans+=p*i
        p+=q
    print(ans)