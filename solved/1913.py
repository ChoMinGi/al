from collections import deque

N = int(input())
K = int(input())

next = 2
lv = 3
board = deque([deque([1])])
while(next<=N*N):
    #upright
    board.appendleft(deque(*[range(next,next+lv-2)]))
    next = next+lv-2
    #down
    for b in board:
        b.append(next)
        next+=1
    #left
    board.append(deque(*[range(next+lv-2,next-1,-1)]))
    next = next+lv-1
    #up
    for b in reversed(board):
        b.appendleft(next)
        next+=1
    lv+=2


for i in range(N):
    for j in range(N):
        if board[i][j]==K:
            loc = [i+1,j+1]
        print(board[i][j],end=' ')
    print()
print(*loc)