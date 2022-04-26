hf,sf,sp=map(int,input().split())
if hf>50 and sf>60 and sp>100:
    print(10)
elif hf>50 and sf>60:
    print(9)
elif sf>60 and sp>100:
    print(8)
elif hf>50 and sp>100:
    print(7)
elif hf>50 or sf>60 or sp>100:
    print(6)
else:
    print(5)