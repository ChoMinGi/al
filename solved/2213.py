import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n = int(input())
w = [0]+list(map(int,input().split()))
graph = defaultdict(list)

for _ in range(n-1):
    s,e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

leaf = set()
for k in graph.keys():
    if len(graph.get(k)) == 1:
        leaf.add(k)

dp = [[0,0] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

start = leaf.pop()

def bfs(n):
    if visited[n]:
        return dp[n]
    
    visited[n] = True
    if n in leaf:
        dp[n] = [0,w[n]]
        return dp[n]
    
    for g in graph[n]:
        if visited[g]:
            continue
        dp[n][0] += max(bfs(g))
        dp[n][1] += bfs(g)[0] 
    dp[n][1]+=w[n]
    return dp[n]

bfs(start)
li = []
res = max(dp[start])
visited = [False for _ in range(n+1)]
def find(m,s):
    visited[m] = True
    if s == dp[m][0]:
        for g in graph[m]:
            if visited[g]:
                continue
            find(g,max(dp[g]))
    else:
        li.append(m)
        for g in graph[m]:
            if visited[g]:
                continue
            find(g,dp[g][0])

find(start,res)
print(max(dp[start]))
print(*sorted(li))