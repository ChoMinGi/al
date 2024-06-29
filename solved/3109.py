import sys

input = sys.stdin.readline

R,C = map(int,input().split())
pipe = []

visited = [[0 for _ in range(C)] for _ in range(R)]
for _ in range(R):
    pipe.append(list(*map(str,input().split())))

res = 0

def dfs(x,y,pipe):
    if x == C-1:
        return True
    if y>0 and pipe[y-1][x+1] == "." and not visited[y-1][x+1]:
        pipe[y-1][x+1] = "x"
        if dfs(x+1,y-1,pipe):
            return True
        pipe[y-1][x+1] = '.'
    if pipe[y][x+1] == "." and not visited[y][x+1]:
        pipe[y][x+1] = "x"
        if dfs(x+1,y,pipe):
            return True
        pipe[y][x+1] = '.'
    if y<R-1 and pipe[y+1][x+1] == "." and not visited[y+1][x+1]:
        pipe[y+1][x+1] = "x"
        if dfs(x+1,y+1,pipe):
            return True
        pipe[y+1][x+1] = '.'
    
    visited[y][x] = 1
    return False    

for h in range(R):
    x = 0
    y = h
    history = []
    if dfs(x,y,pipe):
        res+=1
        

print(res)