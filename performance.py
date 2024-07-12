import time
import random
from heapq import heappush, heappop

def generate_graph(n, m):
    edges = set()
    while len(edges) < m:
        a, b = random.randint(1, n), random.randint(1, n)
        if a != b:
            edges.add((a, b, random.randint(1, 1000)))
    return list(edges)

def prim(n, edges):
    graph = [[] for _ in range(n+1)]
    for a, b, w in edges:
        graph[a].append((w, b))
        graph[b].append((w, a))
    
    visited = [False] * (n+1)
    heap = [(0, 1)]
    mst_weight = 0
    
    while heap:
        w, v = heappop(heap)
        if visited[v]:
            continue
        visited[v] = True
        mst_weight += w
        for nw, nv in graph[v]:
            if not visited[nv]:
                heappush(heap, (nw, nv))
    
    return mst_weight

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    parent = list(range(n+1))
    mst_weight = 0
    
    for a, b, w in edges:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            mst_weight += w
    
    return mst_weight

# 테스트
for n, m in [(100, 1000), (1000, 10000), (10000, 100000)]:
    graph = generate_graph(n, m)
    
    start = time.time()
    prim_result = prim(n, graph)
    prim_time = time.time() - start
    
    start = time.time()
    kruskal_result = kruskal(n, graph)
    kruskal_time = time.time() - start
    
    print(f"N: {n}, M: {m}")
    print(f"Prim: {prim_time:.6f} seconds")
    print(f"Kruskal: {kruskal_time:.6f} seconds")
    print(f"Results match: {prim_result == kruskal_result}\n")