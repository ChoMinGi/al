import sys
from collections import deque

input = sys.stdin.readline

N  = int(input())

ware = []
max_h = 0
max_h_loc = []
for _ in range(N):
    ware.append([*map(int,input().split())])
    
new_ware = sorted(ware, key= lambda x: (-x[1],x[0]))

max_h = new_ware[0][1]
right = new_ware[0]
left = new_ware[0]
res = 0
pole = deque([new_ware[0]])
for x, h in new_ware[1:]:
    if x> right[0]:
        res+=abs(right[0]-x)*h
        right = [x,h]
    elif x< left[0]:
        res+=abs(left[0]-x)*h
        left = [x,h]
    else:
        continue


print(res+max_h)
