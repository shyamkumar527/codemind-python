s=input()
h=int(s[:2])
m=int(s[3:])
if h==12:
    h=0
if m==60:
    m=0
    h+=1
if h>12:
    h-=12;
ha=0.5*(h*60+m)
ma=6*m
ans=abs(ha-ma)
ans= min(360-ans,ans)
print(ans)