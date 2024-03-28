def BF():
    N = int(input())
    is_stack = list(map(int, input().split()))
    orgin = list(map(int, input().split()))
    M = int(input())
    current = list(map(int, input().split()))

    res = []


    for i in range(1,N+1):
        if not is_stack[-i]:
            res.append(orgin[-i])
            if len(res)==M:
                break

    for j in range(M-len(res)):
        res.append(current[j])

    print(" ".join(map(str, res)))



N = int(input())
is_stack = list(map(int, input().split()))
orgin = list(map(int, input().split()))
M = int(input())
current = list(map(int, input().split()))

res = []


for i in range(1,N+1):
    if not is_stack[-i]:
        res.append(orgin[-i])
        if len(res)==M:
            break

for j in range(M-len(res)):
    res.append(current[j])

print(" ".join(map(str, res)))