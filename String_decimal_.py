t=int(input())
for i in range(t):
    s=input()
    for j in s:
        if j.isdigit():
            continue
        else:
            print('False')
            break
    else:
        print('True')