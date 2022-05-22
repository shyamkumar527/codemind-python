a=int(input())
c=0
start=list(map(int,input().split()))
b=int(input())
end=list(map(int,input().split()))
x=int(input())
for i in range(a):
    if start[i]<=x and end[i]>=x:
        c+=1
print(c)