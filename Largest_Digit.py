n=int(input())
dig=0
while n:
    r=n%10
    if r>dig:
        dig=r
    if dig==9:
        break
    n//=10
print(dig)