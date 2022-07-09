s=input()
l=[]
ans=-1
for i in s:
    if i in 'aeiouAEIOU' and i not in l:
        l.append(i)
        print(i,end=' ')
        ans=1
if ans==-1:
    print('-1')