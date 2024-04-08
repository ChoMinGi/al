from collections import deque

N,K = map(int,input().split())
belt = deque(map(int,input().split()))
robot = deque([0 for _ in range(N)])
res = 0
cnt = 1
while(K>0):
    belt.appendleft(belt.pop())
    robot.pop()
    robot.appendleft(0)
    robot[-1]=0
    for i in range(N-2,0,-1):
        if robot[i] and belt[i+1]>=1 and (i+1==N or robot[i+1]==0):
            robot[i]=0
            robot[i+1]=1
            belt[i+1]-=1
            if belt[i+1] == 0:
                res+=1
    if belt[0]>0:
        belt[0]-=1
        if belt[0] == 0:
            res+=1
        robot[0]=1
    if res>=K:
        print(cnt)
        break
    cnt+=1