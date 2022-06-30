def prime(n):
    if n>1:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return 0
        else:
            return 1
    else:
        return 0
n=int(input())
arr=list(map(int,input().split()))
k=int(input())
c=0
for i in arr:
    if(prime(i)) and i>=k:
        c+=1
print(c)