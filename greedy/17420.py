from collections import deque

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

gift = []
res = 0
for i in range(N):
        gift.append([B[i],A[i]])


q = deque(sorted(gift,key=lambda x: (x[0], x[1])))

prev_day = q[0][0]
prev_due = [q[0][1],0]
cnt = 0

print(q)
while(q):
    day,due = q.popleft()

    # new day
    if day != prev_day:
        # need postpone
        day-prev_day+prev_due[0]
            due += 30
            cnt +=1
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
        prev_due = [due,cnt]


print(res)