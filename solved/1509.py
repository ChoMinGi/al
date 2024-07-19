from collections import defaultdict,deque

word = list(*map(str,input().split()))

N = len(word)

graph = defaultdict(list)

for i in range(N):
    l,r = i,i
    while(l >= 0 and r < N and word[l] == word[r]):
        graph[l].append(r+1)
        l-=1
        r+=1
    l,r = i,i+1
    while(l >= 0 and r < N and word[l] == word[r]):
        graph[l].append(r+1)
        l-=1
        r+=1

queue = deque([0])

INF = float("inf")
visited = [INF for _ in range(N+1)]
visited[0] = 0

while(queue):
    now = queue.popleft()
    for next in graph[now]:
        if visited[next]>visited[now]+1:
            visited[next] = visited[now]+1
            queue.append(next)

print(visited[-1])