import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    t = int(input())
    res = t//3+t//2+1
    for i in range(t//3):
        t-=3
        res+=t//2
    print(res)