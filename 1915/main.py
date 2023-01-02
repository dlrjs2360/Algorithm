import sys
import os
path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path+'/input.txt', "r")

n, m = map(int,input().split())
board = [list(map(int,input())) for _ in range(n)]
for i in range(1, n):
    for j in range(1, m):
        if board[i][j] == 1:
            board[i][j] = min(board[i - 1][j - 1], board[i - 1][j], board[i][j - 1]) + 1

# 최대 넓이 구하기
answer = 0
for i in range(n):
    temp = max(board[i])
    answer = max(answer, temp)

print(answer**2)