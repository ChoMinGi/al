import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N,M = map(int,input().split())
visited = [[0 for _ in range(M)] for _ in range(N)]
worth = []
for _ in range(N):
    worth.append([*map(int,input().split())])

def exploration(visited,n,m,where):
    if where==(0,1):
        moves = [[0,1],[1,0]]
    elif where==(0,-1):
        moves = [[0,-1],[1,0]]
    else:
        moves = [[0,1],[0,-1],[1,0]]
    for to_n,to_m in moves:
        next_n = n+to_n
        next_m = m+to_m
        if next_m>=0 and next_m<M and next_n<N:
            if visited[next_n][next_m]<visited[n][m]+worth[next_n][next_m]:
                visited[next_n][next_m] = visited[n][m]+worth[next_n][next_m]
                exploration(visited,next_n,next_m,(to_n,to_m))
            else:
                continue

visited[0][0]=worth[0][0]
exploration(visited,0,0,(0,1))

print(visited[-1][-1])