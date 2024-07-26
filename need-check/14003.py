import sys, bisect
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

start = 0

lis_idx = []
parent = [-1 for _ in range(n)]
actual_values = []

for i in range(n):
    pos = bisect.bisect_left(actual_values ,a[i])
    if pos == len(actual_values):
        actual_values.append(a[i])
        if len(lis_idx)>0:
            parent[i] = lis_idx[-1]
        lis_idx.append(i)
    else:
        actual_values[pos] = a[i]
        lis_idx[pos] = i
        parent[i] = lis_idx[pos-1] if pos>0 else -1

res = []
idx = lis_idx[-1]
while (idx!=-1):
    res.append(a[idx])
    idx = parent[idx]

print(len(res))
print(*res[::-1])