import sys
from collections import deque


def bfs(x, y, cnt):
    queue = deque([(x, y)])
    union = [(x, y)]
    visited[x][y] = cnt
    total_population = A[x][y]
    total_countries = 1

    while queue:
        cx, cy = queue.popleft()

        for dx, dy in moves:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                population_diff = abs(A[cx][cy] - A[nx][ny])
                if L <= population_diff <= R:
                    visited[nx][ny] = cnt
                    queue.append((nx, ny))
                    union.append((nx, ny))
                    total_population += A[nx][ny]
                    total_countries += 1

    # 인구 이동
    new_population = total_population // total_countries
    for ux, uy in union:
        A[ux][uy] = new_population

    return len(union) > 1


N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
moves = [(1, 0), (-1, 0), (0, -1), (0, 1)]
res = 0

while True:
    visited = [[0] * N for _ in range(N)]
    cnt = 1
    any_union_formed = False

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                if bfs(i, j, cnt):
                    any_union_formed = True
                cnt += 1

    if not any_union_formed:
        break

    res += 1

print(res)




def dfs_solve():
    input = sys.stdin.readline

    moves = [[1,0],[-1,0],[0,-1],[0,1]]

    N,L,R = map(int,input().split())
    A = []
    for _ in range(N):
        A.append([*map(int,input().split())])

    moves = [[1,0],[-1,0],[0,1],[0,-1]]
    res = 0
    sw = 1

    while(sw):
        visited = [[0 for _ in range(N)] for _ in range(N)]
        cnt = 1
        visited_dict = dict()
        for i in range(N):
            for j in range(N):
                if visited[i][j] != 0:
                    continue
                temp_sum = 0
                temp_cnt = 0
                stack = [(i,j)]
                visited_set = set(stack)
                while(stack):
                    top = stack.pop()
                    visited_set.remove(top) 
                    if visited[top[0]][top[1]] != 0:
                        continue
                    visited[top[0]][top[1]] = cnt
                    now_A = A[top[0]][top[1]]
                    temp_sum += now_A
                    temp_cnt += 1
                    for move in moves:
                        next_i = top[0]+move[0]
                        next_j = top[1]+move[1]
                        if next_i<0 or next_j<0 or next_i>=N or next_j>=N:
                            continue
                        next_A = A[next_i][next_j]
                        temp_diff = abs(next_A-now_A)
                        if temp_diff>R or temp_diff<L:
                            continue               
                        if (next_i, next_j) not in visited_set:
                            stack.append((next_i, next_j))
                            visited_set.add((next_i, next_j))
                visited_dict[cnt] = temp_sum//temp_cnt
                cnt+=1
        sw = 0

        for i in range(N):
            for j in range(N):
                if A[i][j] != visited_dict[visited[i][j]]:
                    sw = 1
                    A[i][j] = visited_dict[visited[i][j]]
        res+=1
    print(res-1)