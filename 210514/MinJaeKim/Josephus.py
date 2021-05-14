from collections import deque
import sys; input= lambda: sys.stdin.readline().rstrip()
t=int(input())
for _ in range(t):
    d=deque()
    n, k= map(int, input().split())
    for i in range(2,n+1):
        d.append(i)
    cnt=n-1
    while cnt>2:
        d.rotate(-((k-1)%cnt))
        d.popleft()
        cnt-=1
    print(*sorted(d))