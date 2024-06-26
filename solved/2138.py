from collections import deque

N = int(input())
now = [*map(str,input())]
fin = [*map(str,input())]


def is_same(a,b):
    if a == b:
        return True
    else:
        return False
    
queue = deque([[now,0,0]])
res = 0
while(queue):
    top = queue.popleft()
    i = top[2]
    if not is_same(fin[max(0,i-4):max(0,i-1)],top[0][max(0,i-4):max(0,i-1)]):
        continue
    if is_same(top[0],fin):
        res = top[1]
        break
    # none
    queue.append([top[0][:],top[1],i+1])
    # change
    for s in range(max(0,i-1),min(N,i+2)):
        if top[0][s] == "1":
            top[0][s] = "0"
        else:
            top[0][s] = "1"
    queue.append([top[0],top[1]+1,i+1])
    i+=1

    if not queue and (i<N-1):
        res = -1

print(res)