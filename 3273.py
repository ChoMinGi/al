n = int(input())
a = map(int, input().split())
x = int(input())

a = sorted(a)
start = 0
end = n-1
res = 0
while start!=end:
    now = a[start]+a[end]
    if now > x:
        end-=1
    elif now < x:
        start+=1
    else:
        res+=1
        start+=1

print(res)