from collections import Counter

n = int(input())
ngf = list(map(int,input().split()))

nge= []
cnt = Counter(ngf)
for i in ngf:
    nge.append([i,cnt[i]])
stack = [nge[-1]]
res = [-1]

for i in nge[-2::-1]:
    while(1):
        top = stack.pop()
        if i[1] < top[1]:
            res.append(top[0])
            stack.append(top)
            stack.append(i)
            break
        if not len(stack):
            res.append(-1)
            stack.append(i)
            break

print(' '.join(map(str,res[::-1])))