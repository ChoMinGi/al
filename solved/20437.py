import sys
from collections import Counter

input = sys.stdin.readline

inf = int(1e9)
result = []

T = int(input())
for _ in range(T):
    W_dict = dict()
    res = [inf,0]
    for i,l in enumerate(*map(str,input().split())):
        if l not in W_dict.keys():
            W_dict[l] = [i]
        else:
            W_dict[l].append(i)
    K = int(input())
    cnt = 1
    for k,v in W_dict.items():
        if len(v)<K:
            continue
        cnt = 0
        for j in range(len(v)+1-K):
            res[1] = max(res[1],v[j+K-1]-v[j]+1)
            res[0] = min(res[0],v[j+K-1]-v[j]+1)
    if cnt:
        print(-1)
    else:
        print(*res)
