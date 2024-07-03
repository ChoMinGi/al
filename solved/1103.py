import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline
inf = int(100000000)

N,M = map(int,input().split())
coin = []
visited = [[0 for _ in range(M)]for _ in range(N)]
max_value = [[-1 for _ in range(M)]for _ in range(N)]

for _ in range(N):
    coin.append(list(*map(str,input().split())))

visited[0][0] = 1

du = [1,-1,0,0] 
dv = [0,0,1,-1] 

res = 1

def dfs(v,u):
    if max_value[v][u] != -1:
        return max_value[v][u]

    move = 1
    X = int(coin[v][u])
    for i in range(4):
        nu = u + du[i]*X
        nv = v + dv[i]*X
        if nu < 0 or nv < 0 or nu >= M or nv >= N or coin[nv][nu] == "H":
            continue

        if visited[nv][nu]:
            return inf
        visited[nv][nu] = 1
        move = max(move, dfs(nv,nu)+1)
        visited[nv][nu] = 0
    max_value[v][u] = move
    return move

res = dfs(0,0)
if res >= inf:
    print(-1)
else:
    print(res)