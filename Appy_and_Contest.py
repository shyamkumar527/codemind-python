x=int(input())
for i in range(x):
    ans=0
    n,a,b,k=map(int,input().split())
    for j in range(1,n+1):
        if ans>=k:
            break
        if j%a==0 and j%b!=0:
            ans+=1
        elif j%b==0 and j%a!=0:
            ans+=1
    if ans>=k:
        print('Win')
    else:
        print('Lose')