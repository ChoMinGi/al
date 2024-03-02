N = int(input())
H = [int(input()) for _ in range(N)]

stack = []
res =0
td = 0
for h in H:
    while stack and stack[-1][1]<h:
        head, height = stack.pop()
        res+=head+1
        td = 0
    stack.append([td,h])
    td+=1

while stack:
        head, height = stack.pop()
        res+=head+1
print(res)