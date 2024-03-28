stack = []
n = int(input())
for i in range(n):
    td = input().split()
    if len(td) == 2: 
        stack.append(int(td[1])) 
    else:
        order = int(td[0]) 
        if order==2:
            if stack: 
                print(stack.pop())
            else:
                print(-1)
        elif order==3:
            print(len(stack))
        elif order==4:
            if stack:
                print(0)
            else: 
                print(1)
        elif order==5:
            if stack:
                print(stack[-1])
            else:
                print(-1)
