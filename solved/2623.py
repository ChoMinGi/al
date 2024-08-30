from collections import defaultdict,deque
N,M = map(int,input().split())

indegree = [0 for _ in range(N+1)]
graph = defaultdict(list)
for _ in range(M):
    number = list(map(int,input().split()))
    for n in range(1,number[0]):
        graph[number[n]].append(number[n+1])
        indegree[number[n+1]]+=1

start = []
for i in range(1,N+1):
    if indegree[i] == 0:
        start.append(i)
queue = deque(start)

res = []
while(queue):
    top = queue.popleft()
    res.append(top)
    for next in graph[top]:
        indegree[next]-=1
        if indegree[next] == 0:
            queue.append(next)

cnt = 0
for i in indegree:
    if i != 0:
        cnt = 1
        break
if cnt:
    print(0)
else:
    print(*res, sep='\n')