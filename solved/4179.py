def wall(x,y,maze):
    if x < 0 or x >= C or y < 0 or y >= R or maze[y][x] == "#" or maze[y][x] == "F":
         return True
    return False
    
import sys
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize

R,C = map(int, input().split())

maze = []
move = [(-1,0),(1,0),(0,-1),(0,1)]
jihun = []
fire = []
for i in range(R):
    td = list(*map(str, input().split()))
    for j in range(C):
        if td[j] == "J":
            jihun.append([i,j,"J",0])
        elif td[j]== "F":
            fire.append([i,j,"F",0])
    maze.append(td)


j_visited = [[0 for _ in range(C)] for _ in range(R)]
f_visited = [[0 for _ in range(C)] for _ in range(R)]

j_cnt = 1
f_cnt = 1

q = deque(jihun+fire)

while(q):
    y,x,mark,cnt = q.popleft()

    if mark == "J" and not j_visited[y][x]:
        j_visited[y][x] = cnt+1
        for m in move:
            next_x = x+m[0]
            next_y = y+m[1]
            if not wall(next_x,next_y,maze) and not j_visited[next_y][next_x]:
                maze[next_y][next_x] = mark
                q.append([next_y,next_x,mark,cnt+1])

    elif mark == "F" and not f_visited[y][x]:
        f_visited[y][x] = cnt+1
        for m in move:
            next_x = x+m[0]
            next_y = y+m[1]
            if not wall(next_x,next_y,maze) and not f_visited[next_y][next_x]:
                maze[next_y][next_x] = mark
                q.append([next_y,next_x,mark,cnt+1])


res = INF
for i in range(C):
    for j in [0,R-1]:
        td = j_visited[j][i]
        if td and (td<f_visited[j][i] or f_visited[j][i]==0) and res>td :
            res = td
for r in range(1,R-1):
    for s in [0,C-1]:
        td = j_visited[r][s]
        if td and (td<f_visited[r][s] or f_visited[r][s]==0) and res>td:
            res = td

if res == INF:
    print("IMPOSSIBLE")
else:
    print(res)