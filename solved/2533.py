import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())
graph = defaultdict(list)

for _ in range(n-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

leaf = set()
for k in graph.keys():
    if len(graph.get(k)) == 1:
        leaf.add(k)

start = leaf.pop()
visited = [False for _ in range(n+1)]
INF = float('inf')
dp = [[0,0] for _ in range(n+1)]

def bfs(n):
    if visited[n]:
        return dp[n]
    
    visited[n] = True

    if n in leaf:
        dp[n] = [0,1]
        return dp[n]
    
    for next in graph[n]:
        if visited[next]:
            continue
        dp[n][0]+=bfs(next)[1]
        dp[n][1]+=min(bfs(next))
    dp[n][1]+=1
    return dp[n]

bfs(start)

print(min(dp[start]))