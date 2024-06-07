import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())
paper = []

moves = [[0,1],[0,-1],[-1,0],[1,0]]
def find_max_sum(i,j):
    max = paper[i][j]
    td = [max,[i,j]]
    for move in moves:
        next_i = i+move[0]
        next_j = j+move[1]
        if next_i>=0 and next_i<N and next_j>=0 and next_j<M:
            next_num = paper[next_i][next_j]
            td.append([next_i,next_j])
            td[0] += next_num
    