s=input()
res=''
for i in s:
    x=int(i)
    if x%2!=0:
        a=pow(x,2)
        res+=str(a)
print(res)