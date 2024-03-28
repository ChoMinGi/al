import sys
from collections import deque
input = sys.stdin.readline

def find_farthest(start):
    visited = [0 for _ in range(n+1)]
    stack = deque([(start,0)])
    res = 0
    farthest = None
    while(stack):
        now, distance = stack.pop()
        if not visited[now]:
            visited[now] = 1
            if res<distance:
                res = distance
                farthest = now
            for v, d in tree[now]:
                if not visited[v]:
                    stack.append((v,distance+d))
    return farthest, res

n = int(input())
tree = [[] for _ in range(n+1)]
start = 0
for _ in range(n):
    v_list = list(map(int ,input().split()))
    tree[v_list[0]] = [(v_list[i],v_list[i+1]) for i in range(1,len(v_list)-1,2)]
    if len(tree[v_list[0]])==1 and not start:
        start = v_list[0]

f,_ = find_farthest(start)
s,res = find_farthest(f)

print(res)

