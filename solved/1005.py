import sys
from collections import defaultdict, deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N,K = map(int,input().split())
    D = list(map(int,input().split()))
    graph = defaultdict(list)
    incoming_edge = [0 for _ in range(N+1)]
    for _ in range(K):
        a,b = map(int,input().split())
        incoming_edge[b]+=1
        graph[a].append(b)
    W = int(input())
    dp = [0 for _ in range(N+1)]

    start_node = []
    for i in range(1,N+1):
        if incoming_edge[i]==0:
            start_node.append(i)
            dp[i] = D[i-1]

    queue = deque(start_node)

    while(queue):
        now = queue.popleft()
        for n in graph[now]:
            incoming_edge[n]-=1
            dp[n] = max(dp[n], dp[now]+D[n-1])
            if incoming_edge[n] == 0:
                if n == W:
                    break
                queue.append(n)

    print(dp[W])