s=input()
sum=0
dig='0123456789'
for i in s:
    if i in dig:
        sum+=int(i)
print(sum)