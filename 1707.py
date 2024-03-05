import sys 
from collections import deque
input = sys.stdin.readline

K =int(input())
for _ in range(K):
    V,E = map(int, input().split())
    bfs = [[] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    res = "YES"
    for _ in range(E):
        u, v = map(int, input().split())
        bfs[u].append(v)
        bfs[v].append(u)
    sw = -1
    cnt = 1
    for i in range(V):
        queue = deque()
        td = deque()
        if not visited[i]:
            queue.append(i)
            visited[i] = cnt
        while queue:
            s = queue.popleft()
            cnt = visited[s]*sw
            for i in bfs[s]:
                if not visited[i]:
                    visited[i] = cnt
                    td.append(i)
                else:
                    if visited[i] != cnt:
                        res = "NO"
            if not queue:
                queue = td
                td = deque()
    print(res)