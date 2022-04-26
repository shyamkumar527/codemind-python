n=int(input())
pro=1
summ=0
while n:
    r=n%10
    pro=pro*r
    summ+=r
    n=n//10
res=pro-summ
print(res)