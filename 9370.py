import sys
import heapq
input = sys.stdin.readline
INF  = int(1e9)

def short_route(s,gragh,n):
    distances = [INF for _ in range(n+1)]
    distances[s] = 0
    queue = []
    heapq.heappush(queue, [0,s])
    while(queue):
        current_distance, current_intersact = heapq.heappop(queue)
        if current_distance>distances[current_intersact]:
            continue
        for next_intersact, weight in gragh[current_intersact]:
            distance = current_distance + weight
            if distances[next_intersact]>distance:
                distances[next_intersact] = distance
                heapq.heappush(queue,[distance,next_intersact])
    return distances


T = int(input())
res = []
for _ in range(T):
    n,m,t = map(int,input().split())
    s,g,h = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,d = map(int,input().split())
        graph[a].append([b,d])
        graph[b].append([a,d])
        
    s_dij = short_route(s,graph,n)
    g_dij = short_route(g,graph,n)
    h_dij = short_route(h,graph,n)
    print(s_dij)
    td = []
    for _ in range(t):
        x = int(input())
        dij_dis = int(s_dij[x])
        smell_dis = min((int(s_dij[g])+int(g_dij[h])+int(h_dij[x])),int(s_dij[h])+int(h_dij[g])+int(g_dij[x]))
        if dij_dis == smell_dis:
            td.append(x)
        else:
            continue
    res.append(' '.join(map(str,sorted(td))))

print(*res,sep='\n')