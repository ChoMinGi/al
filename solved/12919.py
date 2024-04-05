from collections import deque
S = str(input())
T = [*input()]

bfs = [T]
bfs = deque(bfs)
td = []
res = 0
while(bfs):
    top = bfs.popleft()
    if len(top) == len(S):
        if ''.join(top)==S:
            res+=1
        continue
    if top[0]=='A' and top[-1]=='A': #돌리기X
        td.append(top[:-1])
    if top[0]=='A' and top[-1]=='B': #불가능
        res+=0
    if top[0]=='B' and top[-1]=='B': #무조건 돌린거
        td.append(top[1:][::-1])
    if top[0]=='B' and top[-1]=='A':
        td.append(top[1:][::-1]) #돌렸거나
        td.append(top[:-1]) #A를 뺐거나
    if not bfs:
        bfs = deque(td)
        td = []
        

if res>=1:
    print(1)
else:
    print(0)