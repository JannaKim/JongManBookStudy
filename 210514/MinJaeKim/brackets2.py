import sys; input= lambda: sys.stdin.readline().rstrip()
t= int(input())
for _ in range(t):
    s= list(input())
    stc=[]
    flag=False
    for el in s:
        if el=='(':
            stc.append(')')
        elif el=='{':
            stc.append('}')
        elif el=='[':
            stc.append(']')
        else:
            if not stc:
                flag=True
                break
            ths=stc.pop()
            if ths!=el:
                flag=True
                break
    if flag or stc:
        print('NO')
    else:
        print('YES')
