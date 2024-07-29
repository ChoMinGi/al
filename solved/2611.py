import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N = int(input())
M = int(input())

indegree = [0 for _ in range(N+2)]
graph = defaultdict(list)
for _ in range(M):
    p,q,r = map(int,input().split())
    if q == 1:
        q = N+1
    graph[p].append([r,q])
    indegree[q]+=1

queue = deque([[0,1,[1]]])

visited = [[0,[]] for _ in range(N+2)]

while(queue):
    len, now, q = queue.popleft()
    for cost, node in graph[now]:
        if visited[node][0]<len+cost:
            visited[node][0] = len+cost
            visited[node][1] = q+[node]
        indegree[node]-=1
        if indegree[node] == 0:
            queue.append([visited[node][0],node,visited[node][1]])

print(visited[N+1][0])
print(*visited[N+1][1][:-1]+[1])