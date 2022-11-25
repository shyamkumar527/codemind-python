def prime(n):
    if n<2:
        return 0
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
ans=0
for i in range(2,n):
    for j in range(2,n):
        if i!=j and i*j==n:
            if(prime(i) and prime(j)):
                ans=1
                print(i,j)
                break
    if ans==1:
        break
if ans==0:
    print("-1")