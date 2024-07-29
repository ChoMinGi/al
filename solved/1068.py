from collections import defaultdict, deque

N = int(input())
child = list(map(int,input().split()))
T = int(input())

graph = defaultdict(list)

root = -1

node = [0 for _ in range(N)]
for i in range(N):
    graph[child[i]].append(i)
    node[child[i]]+=1
    if child[i] == -1:
        root = i
node[-1]-=1

queue = deque([T])
node[child[T]]-=1
deleted = []
while(queue):
    now = queue.popleft()
    deleted.append(now)
    for n in graph[now]:
        node[now]-=1
        queue.append(n)

for d in deleted:
    node[d] = 1

res = 0
for n in node:
    if n == 0:
        res +=1
print(res)