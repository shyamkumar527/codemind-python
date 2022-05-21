n=int(input())
arr=list()
count=0
for i in range(n):
    x=int(input())
    arr.append(x)
p=int(input())
for i in arr:
    if i>p:
        count+=2
    else:
        count+=1
print(count)