import sys
import math

def calculate_distance(s,e):
    if mem_dis[s][e]!=0:
        return mem_dis[s][e]
    x1, y1, x2, y2 = loc[s][0],loc[s][1],loc[e][0],loc[e][1]
    mem_dis[s][e] = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return mem_dis[s][e]

input = sys.stdin.readline
INF = float('inf')

N = int(input())

loc = []
for _ in range(N):
    loc.append(list(map(int,input().split())))
mem_dis = [[0 for _ in range(N)]for _ in range(N)]
mem = [[0 for _ in range((1<<N))]for _ in range(N)]

def TSP(s,BM):
    # 순회 끝냈을때
    if BM == (1<<N)-1:
        return calculate_distance(s,0)

    if mem[s][BM]:
        return mem[s][BM]
    
    min_trip = INF
    # 순회중
    
    for e in range(N):
        # 방문하지 않은 경우
        if not (BM & (1<<e)):   
            min_trip = min(min_trip, calculate_distance(s,e) + TSP(e, (BM | (1<<e))))
    mem[s][BM] = min_trip
    return min_trip

res = TSP(0,1)
print(res)

