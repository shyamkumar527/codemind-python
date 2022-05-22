n=int(input())
arr=list(map(int,input().split()))
extra=int(input())
large=max(arr)
for i in arr:
    if (i+extra)>=large:
        print('True',end=' ')
    else:
        print('False',end=' ')