n=int(input())
arr=list(map(int,input().split()))
even=[]
odd=[]
e=o=0
for i in arr:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
evenlen=len(even)
oddlen=len(odd)
for i in range(n):
    if e>=evenlen and o>=oddlen:
        break
    elif e>=evenlen:
        print(odd[o],end=' ')
        o+=1
    elif o>=oddlen:
        print(even[e],end=' ')
        e+=1
    else:
        print(even[e],end=' ')
        e+=1
        print(odd[o],end=' ')
        o+=1
if n%2!=0:
    print('0')