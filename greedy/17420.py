from collections import deque

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

gift = []
res = 0
for i in range(N):
    if A[i]<B[i]:
        cnt = (B[i]-A[i])//30+1
        margin = (A[i]-B[i])+30*cnt
        gift.append([B[i],margin,cnt])
        res+=cnt
    else:
        cnt = (A[i]-B[i])//30
        margin = (A[i]-B[i])%30
        gift.append([B[i],margin,cnt])


q = deque(sorted(gift,key=lambda x: (x[0], x[1])))
prev_day = q[0][0]
prev_due = [q[0][1],q[0][2]]
sw = 0

print(q)
while(q):
    day, m, cnt = q.popleft()
    # new day
    if day != prev_day:
        sw = 0
        # need postpone
        while(prev_due[0]<=cnt-1):
            sw +=1
        if prev_due[1]>m:
            sw +=1
        if prev_due[0]:
            res+=sw
        else:
            sw = 0
        prev_day = day
    #same day
    else:
        if sw:
            res+=sw
    if q and day != q[0][0]:
        prev_due = [m,cnt]


print(res)