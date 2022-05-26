n=int(input())
a=list(map(int,input().split()))
t=int(input())
if t not in a:
    i1=-1
    i2=-1
else:
    i1=a.index(t)
    for i in range(n-1,-1,-1):
        if a[i]==t:
            i2=i
            break
print(i1,i2)