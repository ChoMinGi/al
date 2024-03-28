series = list(input())
boom = str(input())

stack = []

for i in series:
    stack.append(i)
    if ''.join(stack[-len(boom):]) == boom:
        for _ in range(len(boom)):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")