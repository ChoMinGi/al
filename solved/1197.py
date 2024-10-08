import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

V,E = map(int,input().split())

def kruskal():
    graph = []
    for _ in range(E):
        graph.append(list(map(int,input().split())))
    graph.sort(key= lambda x: x[2],reverse=True)

    parent = [i for i in range(V+1)]
    res = []

    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]

    while(graph):
        if len(res) == V:
            break
        a,b,c = graph.pop()
        a_root = find(parent,a)
        b_root = find(parent,b)
        if a_root != b_root:
            parent[a_root] = b_root
            res.append(c)

    print(sum(res))


def krim():
    graph = defaultdict(list)
    for _ in range(E):
        a,b,c = map(int,input().split())
        graph[a].append([c,b])
        graph[b].append([c,a])

    visited = [0 for _ in range(V+1)]
    res = []

    queue = [[0,1]]
    heapq.heapify(queue)


    while(queue):
        if len(res) == V:
            break
        v, now = heapq.heappop(queue)
        if not visited[now]:
            visited[now] = 1
            res.append(v)
            for cost, next in graph.get(now):
                if not visited[next]:
                    heapq.heappush(queue,[cost,next])


    print(sum(res))