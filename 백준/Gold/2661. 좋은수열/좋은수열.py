n = int(input())

def check(snum):
    for i in range(1,len(snum)//2+1):
        if snum[-i:] == snum[-i*2:-i]: return True
    return False

def DFS(num):
    global answer
    snum = str(num)
    if check(snum): return -1
    if len(snum) == n:
        print(num)
        return 0
    for i in range(1,4):
        if DFS(num*10+i) == 0: return 0

DFS(1)
