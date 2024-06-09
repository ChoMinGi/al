from collections import deque

N,K = map(int,input().split())
plug = deque(list(map(int,input().split())))

now = []

plug_key = deque(list(dict.fromkeys(plug).keys()))

cnt = 0
sw = 0
now = []
for _ in range(N):
    if plug_key:
        now.append(plug_key.popleft())
    else:
        sw = 1

while (plug):
    next = plug.popleft()
    if next in now:
        continue
    else:
        plug_key = deque(list(dict.fromkeys(plug).keys()))
        td = [0,None]
        for i in now:
            if i not in plug_key:
                now[now.index(i)] = next
                cnt+=1
                td[1] = None
                break
            elif i in plug_key and plug_key.index(i)>=td[0]:
                td = [plug_key.index(i),i]
        if td[1] is not None:
            now[now.index(td[1])] = next
            cnt+=1
if sw:
    print(0)
else:
    print(cnt)

