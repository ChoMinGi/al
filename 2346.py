from collections import deque

n = int(input())

ballon = deque(list(map(int, input().split())))
ballon_with_index = deque([[value, index+1] for index, value in enumerate(ballon)])

res = []

while(len(ballon_with_index)>1):
    data = ballon_with_index.popleft()
    if data[0]>0:
        for _ in range(data[0]-1):
            ballon_with_index.append(ballon_with_index.popleft())
    else:
        for _ in range(-data[0]):
            ballon_with_index.appendleft(ballon_with_index.pop())
    res.append(data[1])

res.append(ballon_with_index[0][1])

print(" ".join(map(str, res)))