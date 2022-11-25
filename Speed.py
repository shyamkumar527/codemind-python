for i in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    if n==1:
        print("1")
    else:
        a=1
        for i in range(1,n):
            if arr[i-1]>arr[i]:
                a+=1
        print(a)