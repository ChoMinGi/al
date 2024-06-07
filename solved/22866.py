import sys
from collections import deque

input = sys.stdin.readline

N  = int(input())
building = list(map(int,input().split()))
check = [[] for _ in range(N+1)] #거리, 번호, 개수

stack = deque([[0,-1]]) #높이, 번호

for i in range(N):
    now = building[i]
    while(stack and stack[-1][0]<=now):
        stack.pop()
    if stack:
        diff = (i+1)-stack[-1][1]
        check[i+1]=[diff,stack[-1][1],len(stack)]
    stack.append([now,i+1])


stack = deque([[0,-1]]) #높이, 번호
for j in range(N-1,-1,-1):
    now = building[j]
    while(stack and stack[-1][0]<=now):
        stack.pop()
    if stack:
        diff = stack[-1][1]-(j+1)
        if not check[j+1]:
            check[j+1]=[diff,stack[-1][1],len(stack)]
        else:
            if check[j+1][0]>diff:
                check[j+1][1] = stack[-1][1]
            check[j+1][2]+=len(stack)
    stack.append([now,j+1])

for res in check[1:]:
    if res:
        print(res[2],res[1])
    else:
        print(0)