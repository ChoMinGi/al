import sys

input = sys.stdin.readline

N,D = map(int,input().split())
short_cut = [[] for _ in range(D+1)]
distance = [i for i in range(D+1)]


for _ in range(N):
    s,e,d = map(int,input().split())
    if d<e-s and e<=D:
        short_cut[s].append([e,d])
while(short_cut[0]):
        end,dist = short_cut[0].pop()
        distance[end] = min(distance[end],distance[0]+dist)
for i in range(1,D+1):
    distance[i] = min(distance[i],distance[i-1]+1)
    while(short_cut[i]):
        end,dist = short_cut[i].pop()
        distance[end] = min(distance[end],distance[i]+dist)
print(distance[-1])