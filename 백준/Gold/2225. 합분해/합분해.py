n,k = map(int,input().split())

'''
k == 1
0 1 2 3 4 5
1 1 1 1 1 1
-----
k == 2
0 1 2 3 4 5
1 2 3 4 5 6  ==> answer[n-1] + 1
1 1 1 1 1 1
-----
k == 3
0 1 2 3  4  5
1 3 6 10 15 21 ==> answer[n-1]+(n+1)
1 2 3 4  5  6
-----
k == 4
0 1 2  3  4
1 4 10 20    ==> answer[n-1]+p[k-1]
1 3 6  10
'''

p = [[1]*(n+1)] + [[1]+[0]*n for _ in range(k-1)]
for i in range(1,k):
    for j in range(1,n+1):
        p[i][j] = p[i][j-1]+p[i-1][j]

print(p[-1][-1] % 1000000000)