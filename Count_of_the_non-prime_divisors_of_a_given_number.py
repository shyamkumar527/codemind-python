def prime(n):
    if n<2:
        return 1
    else:
        for j in range(2,(n//2)+1):
            if n%j==0:
                return 1
        else:
            return 0
            
n=int(input())
div=list()
c=0
for i in range(1,n+1):
    if n%i==0:
        div.append(i)
for i in div:
    if(prime(i)):
        c+=1
print(c)