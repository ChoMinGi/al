import sys 
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N,R,Q = map(int,input().split())
tree = defaultdict(list)

for _ in range(N-1):
    U,V = map(int,input().split())
    tree[U].append(V)
    tree[V].append(U)

root_node = []
for _ in range(Q):
    root_node.append(int(input()))

visited = [-1 for _ in range(N+1)]
visited[R] = 0

def dfs(now, nodes):
    cnt = 1
    visited[now] = 0
    while(nodes):
        node = nodes.pop()
        if visited[node] != -1:
            continue
        if len(tree[node]) == 1:
            visited[node] = 1
            cnt += 1
            continue
        cnt += dfs(node,tree[node])
    visited[now] = cnt 
    return visited[now]
    
dfs(R, tree[R])

for rn in root_node:
    print(visited[rn])