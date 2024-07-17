import sys

input = sys.stdin.readline

N = int(input())

poly = []
for _ in range(N):
    poly.append([*map(int,input().split())])
poly.append([*poly[0]])

res = 0.0
for i in range(N):
    res+= (poly[i][0]*poly[i+1][1])-(poly[i+1][0]*poly[i][1])

print(round(abs(res*0.5),1))