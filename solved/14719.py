H,W = map(int,input().split())
water = list(map(int,input().split()))

res = 0

for i in range(1,W-1):
    left = max(water[:i])
    right = max(water[i+1:])
    now = min(left,right)
    if now > water[i]:
        res += now - water[i]

print(res)