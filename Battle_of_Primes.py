def prime(n):
    if n<2:
        return 0
    else:
        for k in range(2,(n//2)+1):
            if n%k==0:
                return 0
        else:
            return 1
            
n1=int(input())
n2=int(input())
c=n1+n2
for i in range(c+1,10000):
    if(prime(i)):
        ans=i
        break
print(ans-c)