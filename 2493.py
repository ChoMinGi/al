N = int(input())
tower = list(map(int, input().split()))

stack = []
res = [0 for _ in range(N)]
for i in range(N,-1,-1):
    print(stack, res)
    now = tower[i-1]
    if not stack or stack[-1][0]>now:
        stack.append([now,i-1])
    else:
        while(stack and stack[-1][0]<now):
            top,idx = stack.pop()
            res[idx] = i
        stack.append([now,i-1])

print(*res)