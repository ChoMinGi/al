n = int(input())
nge = list(map(int,input().split()))

stack =[nge[-1]]
res =[-1]
for i in nge[-2::-1]:
    while(1):
        top = stack.pop()
        if i < top:
            res.append(top)
            stack.append(top)
            stack.append(i)
            break
        if not len(stack):
            res.append(-1)
            stack.append(i)
            break

print(' '.join(map(str,res[::-1])))