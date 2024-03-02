n = int(input())
histo = []



for _ in range(n):
    histo.append(int(input()))
prev = 0
res = 0
stack = []
for i, h in enumerate(histo):
    start = i
    while stack and stack[-1][1]>h:
        idx, height = stack.pop()
        res = max(res, (i-idx)*height)
        start = idx
    stack.append([start,h])

for idx, h in stack:
    res = max(res, (n-idx)*h)
print(res)