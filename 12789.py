n = int(input())
row = list(map(int, input().split()))[::-1]
space = []
res=0
for i in range(1,n+1):
    while(1):
        if not row and space:
            if space[-1] != i:
                res = "Sad"
                break
            else:
                space.pop()
                break
        if row[-1] == i:
            row.pop()
            break
        if space and space[-1] == i:
            space.pop()
            break
        else:
            space.append(row.pop())
if res:
    print(res)
else:
    print("Nice")
