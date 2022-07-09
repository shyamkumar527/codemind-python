n=int(input())
arr=list(map(int,input().split()))
ans=su=0
for i in arr:
    su+=i
avg=su/n
print("%.2f" %avg)