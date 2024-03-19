import sys

input = sys.stdin.readline

N, M = map(int,input().split())
city_map = [[] for _ in range(N)]
for _ in range(M):
    s,e,v = map(int,input().split())
    city_map[s].append(e,v)