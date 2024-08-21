import sys
from collections import defaultdict,deque

input = sys.stdin.readline

N = int(input())
graph = defaultdict(list)

for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(N+1)]
visited[1] = True

bfs = list(map(int,input().split()))

queue = deque([1])
res = 1

if bfs[0] != 1:
    print(0)
    sys.exit()

bfs = deque(bfs[1:]) 

while queue and res:
    now = queue.popleft()
    td = [n for n in graph[now] if not visited[n]]
    td = set(td)

    for _ in range(len(td)):
        if not bfs:
            res = 0
            break
        
        next = bfs.popleft()
        if next in td:
            visited[next] = True
            queue.append(next)
        else:
            res = 0
            break

print(res)
