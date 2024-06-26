import sys

input = sys.stdin.readline

N,L = map(int,input().split())
water = []
for _ in range(N):
    s,f =map(int,input().split())
    water.append([s,f])
water= sorted(water,key= lambda x: x[0])

res = 0
td = -1
for s,f in water:
    if td>=s:
        s = td
    if s<f:
        if not (f-s)%L:
            res += (f-s)//L
            s = f
        else:
            res+= (f-s)//L+1
            s = f + (L - ((f-s)%L))
    if s>f:
        td = s

print(res)