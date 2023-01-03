import sys
import os
path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path+'/input.txt', "r")

n, e = map(int,input().split())

graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int,input().split())
    graph[a][b] = c
    graph[b][a] = c

v1, v2 = map(int,input().split())

