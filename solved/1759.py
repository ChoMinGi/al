import sys
from itertools import combinations

input = sys.stdin.readline

L,C = map(int,input().split())

vow = [ord("a"),ord("e"),ord("i"),ord("o"),ord("u")]

pw = list(map(ord,input().split()))

res = set()

fin_vow = []
for p in pw:
    if p in vow:
        fin_vow.append(p)

for c in combinations(pw,L):
    td = 0
    for fv in fin_vow:
        if fv in c:
            td+=1
    if 0<td<L-1:
        string = ""
        for j in sorted(c):
            string+=chr(j)
        res.add(string)

print(*sorted(res),sep='\n')