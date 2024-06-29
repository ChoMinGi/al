import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
ramen = defaultdict(list)

for _ in range(N):
    due, each = map(int,input().split())
    ramen[due].append(each)

due_list = sorted(ramen.keys(),reverse=True)
prev_k = due_list[0]
ramen_list = sorted(ramen.get(prev_k))
res = 0

for k in due_list[1:]:
    for _ in range(prev_k-k):
        if not ramen_list:
            break
        res += ramen_list.pop()
    ramen_list += sorted(ramen.get(k))
    ramen_list = sorted(ramen_list)
    prev_k = k

for _ in range(k):
    if not ramen_list:
        break
    res += ramen_list.pop()

print(res)
