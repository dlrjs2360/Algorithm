import bisect
n = int(input())
arr = list(map(int,input().split()))
stack = []

for x in arr:
    if not stack or x > stack[-1]:
        stack.append(x)
        continue
    stack[bisect.bisect_left(stack,x)] = x

print(n-len(stack))