import sys 
from collections import defaultdict
import heapq

input = sys.stdin.readline

N,M = map(int,input().split())
graph = defaultdict(list)
for _ in range(M):
    a,b,t = map(int,input().split())
    graph[a].append([b,t])
    graph[b].append([a,t])

INF = float("inf")
visited = [INF for _ in range(N+1)]


visited[1] = 0
queue = [[0,1]]
heapq.heapify(queue)
history = []

while(queue):
    v, now = heapq.heappop(queue)
    history.append(now)
    if now == N:
        break
    for next, next_v in graph[now]:
        if visited[next]>visited[now]+next_v:
            visited[next] = visited[now]+next_v
            heapq.heappush(queue,[visited[next]+next_v,next])

min_dis = visited[-1]


def police_dijkstra(s,e):
    queue = [[0,1]]
    heapq.heapify(queue)
    visited = [INF for _ in range(N+1)]
    visited[1] = 0
    while(queue):
        v, now = heapq.heappop(queue)
        if now == N:
            break
        for next, next_v in graph[now]:
            if (now == s and next == e) or (now == e and next == s):
                continue
            if visited[next]>visited[now]+next_v:
                visited[next] = visited[now]+next_v
                heapq.heappush(queue,[visited[next]+next_v,next])
    return visited[-1]

res = []
for i in range(len(history)-1):
    res.append(police_dijkstra(history[i],history[i+1]))


if INF in res:
    print(-1)
else:
    print(max(res)-min_dis)