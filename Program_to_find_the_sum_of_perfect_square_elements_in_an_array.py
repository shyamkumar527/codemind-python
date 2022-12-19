n=int(input())
arr=list(map(int,input().split()))
s=0
for i in arr:
    x=1
    while(1):
        if x*x==i:
            s+=i
            break
        elif x*x>i:
            break
        x+=1
print(s)