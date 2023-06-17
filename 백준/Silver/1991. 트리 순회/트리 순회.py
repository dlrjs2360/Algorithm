import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
leftChild = defaultdict(str)
rightChild = defaultdict(str)
for _ in range(n):
    a,b,c = input().split()
    leftChild[a], rightChild[a] = b,c

def DFS(node,status):
    if status == 1: print(node, end = "")
    if leftChild[node] != '.': DFS(leftChild[node],status)
    if status == 2: print(node, end = "")
    if rightChild[node] != '.': DFS(rightChild[node],status)
    if status == 3: print(node, end = "")

for i in range(1,4):
    DFS('A',i)
    print()