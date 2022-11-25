n=int(input())
arr=list(map(int,input().split()))
s=""
for i in arr:
    s+=str(i)
x=int(s)+1
t=str(x)
for i in t:
    print(i,end=" ")