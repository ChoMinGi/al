import sys
from collections import deque
input = sys.stdin.readline

N,M,R = map(int,input().split())

visited = [0 for _ in range(N+1)]

bfs = [ [] for _ in range(N+1)]
for _ in range(M):
    u,v = map(int,input().split())
    bfs[u].append(v)
    bfs[v].append(u)

for i in range(1,N+1):
        bfs[i] = sorted(bfs[i],reverse=False)

def use_queue():
    queue = deque([R])
    visited[R] = 1
    cnt = 2
    while(queue):
        f = queue.popleft()
        for n in bfs[f]:
            if not visited[n]:
                visited[n] = cnt
                cnt+=1
                queue.append(n)

print(*visited[1:],sep='\n')
