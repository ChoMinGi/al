N = int(input())
now = ['0']+list(*map(str,input().split()))+['0']
next = ['0']+list(*map(str,input().split()))+['0']

INF = float('inf')
res = INF

def toggle(i,list):
    for l in [i-1,i,i+1]:
        if list[l]=='0':
            list[l] = '1'
        else:
            list[l] = '0'

n1 = now[:]
cnt = 0
for i in range(2,N+1):
    if next[i-1]!=n1[i-1]:
        toggle(i,n1)
        cnt+=1
if next[N] == n1[N]:
    res = min(res,cnt)

n2 = now[:]
toggle(1,n2)
cnt = 1
for i in range(2,N+1):
    if next[i-1]!=n2[i-1]:
        toggle(i,n2)
        cnt+=1
if next[N] == n2[N]:
    res = min(res,cnt)

if res == INF:
    print(-1)
else:
    print(res)