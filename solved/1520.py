import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

m, n = map(int, input().split())
res = [[-1] * n for _ in range(m)]
maplist = []
for _ in range(m):
    maplist.append(list(map(int, input().split())))

# 상하좌우
around = [[1, 0], [-1, 0], [0, -1], [0, 1]]


def dfs(y, x):
    if y == m - 1 and x == n - 1:
        return 1
    # 일반적인 DFS 방식과 다른 부분
    if res[y][x] != -1:
        return res[y][x]

    res[y][x] = 0

    for td in around:
        ny, nx = y + td[0], x + td[1]

        if 0 <= nx < n and 0 <= ny < m:
            if maplist[y][x] > maplist[ny][nx]:
                res[y][x] += dfs(ny, nx)

    return res[y][x]


print(dfs(0, 0))