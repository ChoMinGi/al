import sys, heapq
from collections import defaultdict

input = sys.stdin.readline

N,M = map(int, input().split())
INF = float('inf')
da = [INF for _ in range(N+1)]
visited = [False for _ in range(N+1)]

graph = defaultdict(list)
for i in range(1,M+1):
    u,v = map(int, input().split())
    graph[u].append([v,i])
    graph[v].append([u,i])

da[1] = 0
queue = [(0,1,0)]
heapq.heapify(queue)

def cal_time(now,next):
    if next>now:
        return next-now
    else:
        return next+M-now

while queue:
    time, now, now_time = heapq.heappop(queue)
    if now == N:
        break
    if visited[now]:
        continue
    visited[now]= True
    for next,next_time in graph[now]:
        if visited[next]:
            continue
        new_time = time+cal_time(now_time,next_time)
        if da[next]>new_time:
            da[next] = new_time
            heapq.heappush(queue,(new_time,next,next_time))

print(da[N])