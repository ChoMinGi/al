from collections import deque
N,K = map(int, input().split())

max = 200001
visited = [-1 for _ in range(max)]

queue = deque([N])
cnt = 0
visited[N] = cnt
td = []
while(queue):
    now = queue.popleft()
    if visited[now]==-1 or visited[now]>cnt:
        visited[now] = cnt
    while(now>-1 and now<max-1):
        if visited[now]==-1 or visited[now]>cnt:
            visited[now] = cnt
        left = now-1
        right = now+1
        if visited[left]==-1 or visited[left]>cnt+1:
            td.append(left)
            visited[left] = cnt+1
        if visited[right]==-1 or visited[right]>cnt+1:
            td.append(right)
            visited[right] = cnt+1
        if not now:
            break
        now*=2
    if not queue:
        cnt+=1
        queue = deque(td)
        td = []
print(visited[K])