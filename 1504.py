from collections import deque

def short_route(s,e):
    visited = [0 for _ in range(N+1)]
    queue = deque([[s,0]])
    visited[s]=0
    while(queue):
        top = queue.popleft()
        for i in dfs[top[0]]:
            td = i[1]+top[1]
            if not visited[i[0]] and i[0]!=s:
                visited[i[0]] = td
                queue.append([i[0],visited[i[0]]])
            else:
                if visited[i[0]] > td:
                    visited[i[0]] = td
    if not visited[e]:
        return -1
    return visited[e]

N, E = map(int, input().split())

dfs = [[] for _ in range(N+1)]
for _ in range(E):
    a,b,c = map(int, input().split())
    dfs[a].append([b,c])
    dfs[b].append([a,c])
v1, v2 = map(int, input().split())

v1_to_v2 = short_route(v1, v2)
if v1_to_v2 == -1:
    print(-1)
else:
    from_1_to_v1 = short_route(1, v1)
    from_v2_to_N = short_route(v2, N)
    from_1_to_v2 = short_route(1, v2)
    from_v1_to_N = short_route(v1, N)
    
    route_1_cost = from_1_to_v1 + v1_to_v2 + from_v2_to_N if from_1_to_v1 != -1 and from_v2_to_N != -1 else float('inf')
    route_2_cost = from_1_to_v2 + v1_to_v2 + from_v1_to_N if from_1_to_v2 != -1 and from_v1_to_N != -1 else float('inf')
    
    total_min_cost = min(route_1_cost, route_2_cost)
    
    if total_min_cost == float('inf'):
        print(-1)
    else:
        print(total_min_cost)
