n=int(input())

# 소수 판별
def isPrime(a):
    if(a<2): return False
    for i in range(2,int(a**0.5)+1):
        if(a%i==0): return False
    return True

def dfs(num):
    if len(str(num))==n: print(num); return
    for i in range(10):
        temp=num*10+i
        if isPrime(temp): dfs(temp)

for i in [2,3,5,7]:dfs(i)