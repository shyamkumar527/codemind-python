s=input()
ma=max(s)
x=400
v="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
for i in s:
    if i in v:
        if ord(i)<x:
            x=ord(i)
            mi=i
print(mi,s.count(mi),ma,s.count(ma))