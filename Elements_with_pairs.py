n=int(input())
arr=list(map(int,input().split()))
print(*arr,end=" ")
if n%2!=0:
    print("0")