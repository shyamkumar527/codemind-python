arr=list(map(int,input().split()))
num1=num2=0
ind1=0
c1=c2=0
for i in arr:
    if i>num1:
        num1=i
        ind1=c1
    c1+=1
for i in arr:
    if c2!=ind1 and i>num2:
        num2=i
    c2+=1
sum=(num1-1)*(num2-1)
print(sum)