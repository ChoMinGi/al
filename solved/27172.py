import sys
from collections import defaultdict


input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
res = [0] * N

card_dict = defaultdict(int)
for idx,c in enumerate(cards):
    card_dict[c] = idx

max_N = int(1000001)
for v in card_dict.keys():
    for nv in range(v*2,max_N,v):
        if nv in card_dict.keys():
            res[card_dict.get(nv)]-=1
            res[card_dict.get(v)] +=1


print(*res)