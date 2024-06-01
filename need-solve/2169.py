import sys

input = sys.stdin.readline

def top_value(top,now):
    LtR = [0 for _ in range(M)]
    RtL = [0 for _ in range(M)]
    LtR[0] = now[0]+top[0]
    for i in range(1,M):
        LtR[i] = now[i] + max(top[i],LtR[i-1])

    RtL[M-1] = now[M-1]+top[M-1]
    for i in range(M-2,-1,-1):
        RtL[i] = now[i]+ max(top[i],RtL[i+1])
    
    res = []
    for i in range(M):
        res.append(max(LtR[i],RtL[i]))
    return res


N,M = map(int,input().split())
mars = []
for _ in range(N):
    mars.append(list(map(int, input().split())))

for i in range(1,M):
    mars[0][i] += mars[0][i-1]

if N == 1:
    print(mars[0][-1])
else:
    for i in range(N-2):
        mars[i+1] = top_value(mars[i],mars[i+1])

    for i in range(M-2,-1,-1):
        mars[-1][i] += mars[-1][i+1]

    res = -2e9
    for i in range(M):
        if res < mars[-1][i]+mars[-2][i]:
            res = mars[-1][i]+mars[-2][i]

    print(res)