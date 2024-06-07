import sys

input = sys.stdin.readline

N = int(input())
request = map(int,input().split())
M = int(input())
sw = 0

request = sorted(request)

for i in range(N):
    left = N-i
    now = request[i]
    maximum = M/left
    if maximum <= now:
        print(M//left)
        sw = 1
        break
    M-=request[i]

if not sw:
    print(request[-1])