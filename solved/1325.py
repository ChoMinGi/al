import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)] 

for _ in range(M):
    u,v = map(int,input().split())
    graph[v].append(u)


def bfs(node):
    visited = [0 for _ in range(N+1)]
    
    q = deque([node])
    visited[node] = 1
    cnt = 0
    while(q):
        top = q.popleft()
        for next in graph[top]:
            if not visited[next]:
                visited[next] = 1
                q.append(next)
                cnt+=1
    return cnt

res = []
max_v = 0
for i in range(1,N+1):
    now = bfs(i)
    if now>max_v:
        res = [i]
        max_v=now
    elif now == max_v:
        res.append(i)

print(*res)