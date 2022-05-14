a=int(input())
even=odd=0
while a:
    r=a%10
    a=a//10
    if r%2==0:
        even+=1
    else:
        odd+=1
if even>0 and odd==0:
    print("Even")
elif even==0 and odd>0:
    print("Odd")
else:
    print("Mixed")