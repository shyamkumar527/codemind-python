def prime(n):
    if n<2:
        return 0
    else:
        for j in range(2,(n//2)+1):
            if n%j==0:
                return 0
        else:
            return 1
            
a=int(input())
b=int(input())
for i in range(a+1,b):
    if prime(i):
        print(i)