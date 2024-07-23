import sys, heapq
from collections import defaultdict


input = sys.stdin.readline

N = int(input())
A = list(map(str,input().split()))

fin = tuple(A)

M = int(input())
C = []
for _ in range(M):
    C.append(list(map(int,input().split())))

dict = defaultdict(int)

queue = [[0,A]]
heapq.heapify(queue)

res = 0

while(queue):
    v, now = heapq.heappop(queue)
    str_now = tuple(now)
    if str_now == fin:
        res = v
        break
    dict[str_now] = v
    for l, r, c in C:
        next = now.copy()
        next[l-1], next[r-1] = next[r-1], next[l-1]
        str_next = tuple(next)
        if dict.get(str_next) is None or dict.get(str_next)>v+c:
            heapq.heappush(queue,[v+c,next])
    
if res!=0:
    print(res)
else:
    print(-1)