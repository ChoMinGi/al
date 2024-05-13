import sys

input = sys.stdin.readline

orgn = list(*map(str,input().split()))

M = int(input())
td = []

for _ in range(M):
    cmd = list(map(str,input().split()))
    if len(cmd)==2:
        orgn.append(cmd[1])
    elif cmd[0] == 'L':
        if orgn:
            td.append(orgn.pop())
    elif cmd[0] == 'D':
        if td:
            orgn.append(td.pop())
    else:
        if orgn:
            orgn.pop()


print(*(orgn+td[::-1]),sep='')
