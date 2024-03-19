from collections import deque
import sys

input = sys.stdin.readline

N, L = map(int,input().split())
dict = {}

subway =[[]]

for i in range(1,L+1):
    td = list(map(int,input().split()))[:-1]
    subway.append(td)
    for s in td:
        if dict.get(s):
            dict[s].add(i)
        else:
            dict[s] = set([i])
            
start, end = map(int,input().split())

transport = [-1 for _ in range(N+1)]
visited = [0 for _ in range(L+1)]
line_list = deque()
transport[start] = 0

for start_line in dict[start]:
    line_list.append(start_line)
    visited[start_line] = 1
cnt =0
td = []
while(line_list):
    now_line = line_list.popleft()
    for station in subway[now_line]:
        if transport[station]== -1:
            transport[station] = cnt
            for new_line in dict[station]:
                if not visited[new_line]:
                    td.append(new_line)
                    visited[new_line]=1

    if not line_list:
        cnt+=1
        line_list = deque(td)
        td = []

print(transport[end])