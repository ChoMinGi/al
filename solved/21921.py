N, X = map(int,input().split())
view = list(map(int,input().split()))

visit = 0
max_visit = 0
cnt = 0

for i in range(N-X+1):
    if i == 0:
        visit = sum(view[:X])
        max_visit = visit
        cnt = 1
        continue
    visit-=view[i-1]
    visit+=view[i-1+X]
    if max_visit == visit:
        cnt +=1

    if max_visit<visit:
        max_visit = visit
        cnt = 1

if max_visit != 0:
    print(max_visit)
    print(cnt)
else:
    print("SAD")