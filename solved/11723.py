import sys
input = sys.stdin.readline

M = int(input())
S = [0 for _ in range(20)]

for _ in range(M):
    td = list(map(str, input().split()))
    if len(td)==1:
        command = td[0]
        if command=="all":
            S = [1 for _ in range(20)]
        else:
            S = [0 for _ in range(20)]
    else:
        command, x = td[0], int(td[1])-1
        if command=="add":
            S[x]=1
        elif command=="remove":
            S[x]=0
        elif command=="check":
            if S[x]==1:
                print(1)
            else:
                print(0)
        else:
            if S[x]==1:
                S[x]=0
            else:
                S[x]=1