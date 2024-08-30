import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
population = list(map(int,input().split()))

graph = defaultdict(list)
for _ in range(N-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

leaf = set()
for k in graph.keys():
    if len(graph.get(k)) == 1:
        leaf.add(k)

start =leaf.pop()
visited = [False for _ in range(N+1)]
dp = [[0,0,False] for _ in range(N+1)]
def tree(n):
    if visited[n]:
        return dp[n]
    visited[n] = True

    if n in leaf:
        dp[n] = [0,population[n-1],False]
        return dp[n]

    for next in graph[n]:
        if visited[next]:
            continue
        x,y,b = tree(next)
        if x>y and b:
            dp[n][0]+=x
        else:
            dp[n][0]+=y
            dp[n][2] = True

        dp[n][1]+=x
    dp[n][1]+=population[n-1]

    return dp[n]

tree(start)
print(max(dp[start]))