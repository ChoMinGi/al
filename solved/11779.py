import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize


n = int(input())
m = int(input())
distance = [[INF,_] for _ in range(n+1)]
city = [[] for _ in range(n+1)]
for _ in range(m):
    u,v,c = map(int,input().split())
    city[u].append([v,c])
s,e = map(int,input().split())

q = []
heapq.heappush(q,[0, s])
distance[s] = [0,[s]]

while(q):
    cost, now = heapq.heappop(q)
    if distance[now][0]<cost:
        continue
    for next, value in city[now]:
        new_cost = cost+value
        if distance[next][0] > new_cost:
            distance[next][0] = new_cost
            distance[next][1] = distance[now][1]+[next]
            heapq.heappush(q,[new_cost, next])

print(distance[e][0])
print(len(distance[e][1]))
print(*distance[e][1])