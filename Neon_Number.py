n=int(input())
pro=n*n
res=0
while pro:
    r=pro%10
    pro=pro//10
    res+=r
if n==res:
    print("Neon Number")
else:
    print("Not Neon Number")