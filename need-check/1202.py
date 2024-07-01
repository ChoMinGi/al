#heapq 복습하기에 좋은듯
#https://www.acmicpc.net/problem/1202

import sys
import heapq

input = sys.stdin.readline

N,K = map(int,input().split())

gem = []
bag = []
for _ in range(N):
    gem.append(list(map(int,input().split())))
for _ in range(K):
    bag.append(int(input()))

gem = sorted(gem, key= lambda x: x[0])
bag = sorted(bag)

max_heapq = []

cnt = 0
res = 0
for b in bag:
    while cnt<N and gem[cnt][0]<=b:
        heapq.heappush(max_heapq,-gem[cnt][1])
        cnt += 1
    
    if max_heapq:
        res+= -heapq.heappop(max_heapq)

print(res)
