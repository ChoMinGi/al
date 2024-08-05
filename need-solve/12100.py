import sys

input = sys.stdin.readline

N = int(input())
width_board = []
length_board = [[] for _ in range(N)] 
for _ in range(N):
    td = list(map(int,input().split()))
    width_board.append(td)
    for i in range(N):
        length_board[i].append(td[i])

def up(board):
    res = []
    for i in range(N):
        stack = []
        if len(stack) == 2:
