n=int(input())
num=0
for i in range(n):
    st=input()
    for j in range(0,len(st),2):
        if st[j]=='+':
            num+=1
        elif st[j]=='-':
            num-=1
print(num)