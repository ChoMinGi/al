N,a,b = map(int,input().split())

if a+b>N+1:
    res = -1
elif a+b == N+1:
    res=[*range(1,a+1)]
    res+=[*range(b-1,0,-1)]
elif a+b == N:
    if a<b:
        a,b = b,a
    res = [*range(1,a+1)]
    res+=[a]
    res+=[*range(b-1,0,-1)]
    if a<b:
        res.reverse()
else:
    res = [*range(1,a+1)]
    res+=[1]*(N-a-b)
    res+=[*range(b,0,-1)]

if res == -1:
    print(-1)
else:
    print(*res,sep=' ')