n=int(input())
l=list(map(int,input().split()))
odd=0
for i in l:
    if i%2==1:
        odd+=1
if odd%2==1:
    print(0)
else:
    print(1)