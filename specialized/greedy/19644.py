import sys
from collections import deque

input = sys.stdin.readline

L = int(input())
Ml, Mk = map(int,input().split())
C = int(input())

sw = 0
q = deque([])

for i in range(L):
    if q and i-q[0]==Ml:
        q.popleft()
        
    now = int(input())
    if q:
        granade = (now / Mk) > (len(q)+1)
    else:
        granade = now > Mk
    if granade:
        if C>0:
            C-=1
        else:
            sw = 1
            break
    else:
        q.append(i)

    
if sw:
    print("NO")
else:
    print("YES")