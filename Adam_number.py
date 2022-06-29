n=int(input())
sq=pow(n,2)
sqcnt=revsqcnt=0
x=sq
while x:
    sqcnt+=1
    x//=10
rev=0
x=n
while x:
    r=x%10
    rev=(rev*10)+r
    x//=10
revsq=pow(rev,2)
x=revsq
while x:
    revsqcnt+=1
    x//=10
x=revsq
ans=0
while x:
    r=x%10
    ans=(ans*10)+r
    x//=10
if ans==sq and sqcnt==revsqcnt:
    print('True')
else:
    print('False')