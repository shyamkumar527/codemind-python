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
mi=min(arr)
ma=max(arr)
c=a=b=0
for i in arr:
    if a==1 and b==1:
        break
    if i==mi:
        a=1
    if i==ma:
        b=1
    if a==1 or b==1:
        if(prime(i)):
            c+=1
print(c)