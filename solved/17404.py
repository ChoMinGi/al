import sys

input = sys.stdin.readline

N = int(input())
INF = float('inf')
color = []
for _ in range(N):
    color.append(list(map(int,input().split())))

dp_r = [[INF for _ in range(3)] for _ in range(N)]
dp_g = [[INF for _ in range(3)] for _ in range(N)]
dp_b = [[INF for _ in range(3)] for _ in range(N)]

dp_r[0] = [color[0][0],INF,INF]
dp_g[0] = [INF,color[0][1],INF]
dp_b[0] = [INF,INF,color[0][2]]

for i in range(1,N):
    for j in range(3):
        dp_r[i][j] = color[i][j]+min(dp_r[i-1][(j+1)%3],dp_r[i-1][(j+2)%3])
        dp_g[i][j] = color[i][j]+min(dp_g[i-1][(j+1)%3],dp_g[i-1][(j+2)%3])
        dp_b[i][j] = color[i][j]+min(dp_b[i-1][(j+1)%3],dp_b[i-1][(j+2)%3])

res = min(dp_r[N-1][1],dp_r[N-1][2],dp_g[N-1][0],dp_g[N-1][2],dp_b[N-1][0],dp_b[N-1][1])

print(res)