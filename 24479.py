N,M,R = map(int,input().split)

visited = [0 for _ in range(N)]

dfs = [ [] for _ in range(N)]
for _ in range(M):
    u,v = map(int,input().split())
    dfs[u].append(v)
    dfs[v].append(u)

queue =[1]
cnt =1
while(queue):
    t = queue.pop()
    if not visited[t] and dfs[t]:
        next = sorted(dfs[t])[0]
        visited[t] = cnt
        cnt+=1
        queue.append(next)
    else:

    