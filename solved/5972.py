import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

N,M = map(int,input().split())

farm = [[] for _ in range(N+1)]
distance = [INF for _ in range(N+1)]

for _ in range(M):
    a,b,c = map(int,input().split())
    farm[a].append([b,c])
    farm[b].append([a,c])

start = 1
distance[start] = 0
q = []
heapq.heappush(q,[0,start])

while(q):
    cost, now = heapq.heappop(q)
    if cost > distance[now]:
        continue
    for next, value in farm[now]:
        next_cost = cost+value
        if distance[next] > next_cost:
            distance[next] = next_cost
            heapq.heappush(q,[next_cost, next])

print(distance[-1])