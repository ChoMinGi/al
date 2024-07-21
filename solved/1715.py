import sys
import heapq

input = sys.stdin.readline

N = int(input())
card = []

for _ in range(N):
    card.append(int(input()))

heapq.heapify(card)

res = 0

while(card):
    f = heapq.heappop(card)
    if not card:
        break
    s = heapq.heappop(card)
    heapq.heappush(card,f+s)
    res+=(f+s)

print(res)