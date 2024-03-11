import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def short_route(s,e):
    distances = [INF for _ in range(N+1)]
    distances[s] = 0
    queue = [(0,s)]
    while(queue):
        dis, node = heapq.heappop(queue)
        for adjacent, w in dfs[node]:
            distance = dis + w
            if distances[adjacent]>distance:
                distances[adjacent] = distance
                heapq.heappush(queue,(distance,adjacent))
    return distances[e]
N, E = map(int, input().split())

dfs = [[] for _ in range(N+1)]
for _ in range(E):
    a,b,c = map(int, input().split())
    dfs[a].append([b,c])
    dfs[b].append([a,c])
v1, v2 = map(int, input().split())

v1_to_v2 = short_route(v1, v2)
from_1_to_v1 = short_route(1, v1)
from_v2_to_N = short_route(v2, N)
from_1_to_v2 = short_route(1, v2)
from_v1_to_N = short_route(v1, N)

route_1_cost = from_1_to_v1 + v1_to_v2 + from_v2_to_N
route_2_cost = from_1_to_v2 + v1_to_v2 + from_v1_to_N

total_min_cost = min(route_1_cost, route_2_cost)

if total_min_cost >= INF:
    print(-1)
else:
    print(total_min_cost)