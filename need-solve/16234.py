import sys
from collections import deque

input = sys.stdin.readline

moves = [[1,0],[-1,0],[0,-1],[0,1]]

N,L,R = map(int,input().split())
visited = [[0 for _ in range(N)] for _ in range(N)]
A = []
for _ in range(N):
    A.append([*map(int,input().split())])

change = 0
change_day = 1
total = 0
country = 0
res = 0
t_A = A
while(True):
    if change_day:
        change_day = 0
        res +=1
    else:
        break

    stack = deque([[0,0,A[0][0]]])
    visited = [[0 for _ in range(N)] for _ in range(N)]
    td = deque([])
    while(stack):
        now_r,now_c,now_A = stack.pop()
        if visited[now_r][now_c]:
            continue  
        visited[now_r][now_c] = res
        total += now_A
        country +=1
        print(total, country)
        for to_r, to_c in moves:
            next_r = now_r+to_r
            next_c = now_c+to_c
            if next_r>=0 and next_r<N and next_c>=0 and next_c<N and not visited[next_r][next_c]:
                next_A = A[next_r][next_c]
                diff = abs(next_A-now_A)
                if diff>=L and diff<=R:
                    change = 1
                    stack.append([next_r,next_c,next_A])
                else:
                    td.append([next_r,next_c,next_A])
        if not stack:
            if not td:
                continue
            if change ==1:
                union = total//country
                print(total, union)
                for r in range(N):
                    for c in range(N):
                        if visited[r][c] == res and t_A[r][c] != union:
                            t_A[r][c] = union
                            change_day = 1
                change = 0
            total = 0
            country = 0
            stack = td
        print(*A , sep='\n')
        print(*visited , sep='\n')
    A = t_A
print(res)