import sys

input = sys.stdin.readline

inf = int(1e9)

N, M = map(int,input().split())
distance = [inf for _ in range(N+1)]
city_map = [list(map(int,input().split())) for _ in range(M)]
distance[1] = 0
is_timeMachine = 0

for _ in range(N-1):
    for a,b,c in city_map:
        if distance[a]!=inf and distance[b]>distance[a]+c:
            distance[b] = distance[a]+c
for a,b,c in city_map:
    if distance[b]is not inf and distance[a]+c<distance[b]:
        is_timeMachine =1
        break


if is_timeMachine:
    print(-1)
else:
    for d in distance[2:]:
        if d >= inf:
            print(-1)
            continue
        print(d)
        

# 3 4
# 1 2 4
# 1 3 3
# 2 3 -1
# 3 1 -2

# 4
# 3

# 음수 가중을 스마트하게 알아낸 방법
N,M=map(int,input().split())
E=[]
for _ in range(M):
    E.append(list(map(int,input().split())))
INF=1e9
D=[INF]*(N+1)

def bf():    
    D[1]=0
    for i in range(N):
        for a,b,c in E:
            if D[a]+c<D[b] and D[a]<INF:
                D[b]=D[a]+c
                if i==N-1:return True
    return False


if bf():print(-1)
else:
    for d in D[2:]:print(d if d<INF else -1)