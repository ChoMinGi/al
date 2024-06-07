import sys

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n)]
values = map(int,input().split())
for _ in range(n):
    u,v = map(int,input().split())
    graph[u] = v
    graph[v] = u
