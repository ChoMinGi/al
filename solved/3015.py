import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

line = []
res = 0
td = 0
e=0
stack = deque([])
for _ in range(n):
    line.append(int(input()))

for h in line:
    while stack and stack[-1][0]<h:
        top, each = stack.pop()
        res+=each
    
    if not stack:
        stack.append([h,1])
        continue

    top, each = stack.pop()
    if top==h:
        res+=each
        if stack:
            res+=1
        stack.append([h,each+1])
        continue
    else:
        stack.append([top,each])
    stack.append([h,1])
    res+=1
print(res)