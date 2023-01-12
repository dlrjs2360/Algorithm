import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
store = [arr[0]]
L = 1

for num in arr:

    if num > store[-1]:
        store.append(num)
        L += 1
        continue

    left = 0
    right = L - 1
    while left <= right:
        mid = (left + right) // 2
        if store[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    store[left] = num


print(L)