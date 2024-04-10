import sys
from collections import deque

input =sys.stdin.readline

n,m = map(int,input().split())
color_map = []
visited = [[None for _ in range(m)] for _ in range(n)]
start = (0,0)
for i in range(n):
    line = list(map(int,input().split()))
    if 2 in line:
        j = line.index(2)
        start = [i,j,0]
    color_map.append(line)

move = ((1,0),(-1,0),(0,1),(0,-1))
queue = deque([start])
visited[start[0]][start[1]] = 0

while(queue):
    now_i,now_j,cnt = queue.popleft()
    if cnt != -1:
        cnt=visited[now_i][now_j]+1
    for to_i, to_j in move:
        next_i = now_i+to_i
        next_j = now_j+to_j
        if next_i>=0 and next_i<n and next_j>=0 and next_j<m and (visited[next_i][next_j] == None or visited[next_i][next_j]<cnt-2):
            if color_map[next_i][next_j] == 0:
                visited[next_i][next_j] =0
                queue.append([next_i,next_j,-1])
                continue
            visited[next_i][next_j] = cnt
            queue.append([next_i,next_j,cnt])

for v in visited:
    print(*v)