import sys, heapq

input = sys.stdin.readline

n = int(input())
lecture = []
for _ in range(n):
    d,p = map(int,input().split())
    lecture.append([p,d])
if not lecture:
    print(0)
    exit()
lecture.sort()
queue = []
heapq.heapify(queue)
res = 0
for d in range(lecture[-1][0],0,-1):
    while(lecture and lecture[-1][0]>=d):
        due,cost = lecture.pop()
        heapq.heappush(queue,[-cost,due])
    if queue:
        top = heapq.heappop(queue)
        res-=top[0]

print(res)