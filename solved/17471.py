from collections import defaultdict,deque

N = int(input())
INF = float("inf")
people = list(map(int,input().split()))

graph = defaultdict(list)
for i in range(1,N+1):
    city = list(map(int,input().split()))
    graph[i] = city[1:]
mask = (1<<N)-1

def is_connect(group):
    visited = set([group[0]])
    queue = deque([group[0]])
    cnt = people[group[0]-1]
    while(queue):
        now = queue.popleft()
        for next in graph[now]:
            if next not in visited and next in group:
                visited.add(next)
                queue.append(next)
                cnt+=people[next-1]
    return cnt, len(group) == len(visited)
    

res = INF

for n in range(1,mask):
    g1 = [i for i in range(1,N+1) if n & (1<<(i-1))]
    g2 = [i for i in range(1,N+1) if not n & (1<<(i-1))]
    
    g1_cnt, g1_connection = is_connect(g1)
    g2_cnt, g2_connection = is_connect(g2)

    if g1_connection and g2_connection:
        res = min(res, abs(g1_cnt-g2_cnt))

if res == INF:
    print(-1)
else:
    print(res)