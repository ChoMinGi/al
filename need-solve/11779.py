import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())
dp = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    u,v,c = map(int,input().split())
    dp[u][v] = c
s,e = map(int,input().split())

queue = deque(s)
td = []
while(queue):
    

    if not queue:
        queue = deque(td)
        td = []