n=int(input())
arr=list(map(int,input().split()))
e=[]
o=[]
ev=od=0
for i in arr:
    if i%2==0:
        e.append(i)
        ev+=1
    else:
        o.append(i)
        od+=1
i=j=0
while(1):
    if i==ev and j==od:
        break
    if i<ev:
        print(e[i],end=" ")
        i+=1
    if j<od:
        print(o[j],end=" ")
        j+=1
if n%2==1:
    print("0")