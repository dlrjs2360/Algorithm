import sys
import os
path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path+'/input.txt', "r")


n,k = map(int,input().split())
arr = list(map(int,input().split()))
idx = [i for i in range(n) if arr[i] == 1]
print( min( idx[i+k-1]-idx[i]+1 for i in range(len(idx)-k+1) )  if len(idx) >= k else -1 )

