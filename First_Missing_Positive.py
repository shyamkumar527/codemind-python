n=int(input())
arr=list(map(int,input().split()))
for i in range(1,100):
    if i not in arr:
        print(i)
        break