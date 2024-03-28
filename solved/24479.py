import sys
input = sys.stdin.readline

N,M,R = map(int,input().split())

visited = [0 for _ in range(N+1)]

dfs = [ [] for _ in range(N+1)]
for _ in range(M):
    u,v = map(int,input().split())
    dfs[u].append(v)
    dfs[v].append(u)

for i in range(1,N+1):
        dfs[i] = sorted(dfs[i],reverse=False)

def rec_dfs(n):
    global cnt
    visited[n] = cnt
    for t in dfs[n]:
        if not visited[t]:
            print(cnt,t)
            cnt +=1
            rec_dfs(t)
cnt = 1
rec_dfs(R)
print(*visited[1:],sep='\n')
        




def use_stack():
    for i in range(1,N+1):
        dfs[i] = sorted(dfs[i],reverse=True)

    cnt = 2
    visited[R] = 1
    stack = [R]
    while(stack):
        top = stack.pop()
        if not visited[top]:
            visited[top] = cnt
            cnt+=1
        for t in dfs[top]:
            if not visited[t]:
                stack.append(t)

    print(*visited[1:],sep='\n')