n = int(input())
row = list(map(int, input().split()))[::-1]
space = [0]
for i in range(1,n+1):
    while(1):
        last = row.pop()
        if last == i:
            break
        elif space[-1] == i:
            space.pop()
            break
        else:
            space.append(last)
            if len(space) == n:
                print("Sad")
                break
            break

print("Nice")
