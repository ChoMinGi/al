import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n,k,t,m = map(int,input().split())
    score = [[0 for _ in range(k+1)] for _ in range(n+1)]
    team = [[0,0,0,i] for i in range(n+1)]
    team[0][0] = -1
    for k in range(m):
        i,j,s = map(int,input().split())
        td = s-score[i][j]
        if td>0:
            team[i][0]+=td
            score[i][j]+=td
        team[i][1]+=1
        team[i][2]=k
    team = sorted(team, key= lambda x: (-x[0],x[1],x[2]))
    for k in range(n+1):
        if team[k][3] == t:
            print(k+1)