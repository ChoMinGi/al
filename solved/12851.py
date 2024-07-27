import sys
from collections import deque
N, K= map(int, sys.stdin.readline().split())
queue = deque()
queue.append(N)
way = [0]*100001
cnt, result = 0,0
while (queue):
    a = queue.popleft()
    temp = way[a]
    if a == K:
        result = temp
        cnt+=1
        continue

    for i in [a-1, a+1, a*2]:
        if 0 <= i < 100001 and (way[i] == 0 or way[i] >= way[a]+1):
            way[i] = way[a]+1
            queue.append(i)

print(result)
print(cnt)