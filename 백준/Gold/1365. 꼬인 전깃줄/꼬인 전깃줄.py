import bisect
n = int(input())
arr = list(map(int,input().split()))
stack = []

for x in arr:
    if not stack or x > stack[-1]:
        stack.append(x)
        continue
    loc = bisect.bisect_left(stack,x)
    stack[loc] = x

print(n-len(stack))