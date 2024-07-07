import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

N,M = map(int,input().split())
homes = defaultdict(list)

start = 0
for _ in range(M):
    A,B,C = map(int,input().split())
    homes[A].append([C,B])
    homes[B].append([C,A])

start = 1


min_heap = [(0,start)]
res = []
visited = [False for _ in range(N+1)]

while(min_heap):
    c, now = heapq.heappop(min_heap)
    if not visited[now]:
        res.append(c)
        visited[now] = True
        if len(res) == N:
            break
        for cost, next in homes[now]:
            if not visited[next]:
                heapq.heappush(min_heap,(cost,next))

print(sum(res)-max(res))