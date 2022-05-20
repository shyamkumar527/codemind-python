a,b=map(int,input().split())
ans=0
if a==1 and b==10:
    print('Yes')
    ans+=1
elif a==10 and b==1:
    print('Yes')
    ans+=1
elif b>1 and b<=10:
    if (a+1)==b:
        print('Yes')
        ans+=1
    elif (a-1)==b:
        print('Yes')
        ans+=1
if ans==0:
    print('No')