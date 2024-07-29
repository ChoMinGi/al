import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N,M = map(int,input().split())

graph = defaultdict(list)

indegree = [0 for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1

queue = deque()
for i in range(1,N+1):
    if indegree[i] == 0:
        queue.append(i)

res = []
while(queue):
    now = queue.popleft()
    res.append(now)
    for node in graph[now]:
        indegree[node] -= 1
        if indegree[node] == 0:
            queue.append(node)

print(*res)