import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

n,m = map(int,input().split())
parent = [*range(n+1)]

def find(n):
    if parent[n]!=n:
        parent[n] = find(parent[n])
    return parent[n]

for _ in range(m):
    s,a,b = map(int,input().split())
    if s == 0:
        parent[find(a)] = parent[find(b)]
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
