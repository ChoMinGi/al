H,W = map(int,input().split())
water = list(map(int,input().split()))

left = 0
res = 0

for i in range(1,len(water)-1):
    if water[left]<=water[i] and water[i]>water[i+1] or i+2 == len(water):
        if water[i]<water[i+1]:
            i+=1
        height = min(water[left],water[i])
        for h in range(left+1,i):
            res+=(height-water[h])
        left = i

if len(water)<=2:
    print(0)
else:
    print(res)