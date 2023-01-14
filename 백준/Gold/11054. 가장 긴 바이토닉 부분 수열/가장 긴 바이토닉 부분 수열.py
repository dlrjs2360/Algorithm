n = int(input())

arr = list(map(int, input().split()))
reverse_case = arr[::-1]

increase = [1 for _ in range(n)] # 가장 긴 증가하는 부분 수열
decrease = [1 for _ in range(n)] # 가장 긴 감소하는 부분 수열(reversed)

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            increase[i] = max(increase[i], increase[j]+1)
        if reverse_case[i] > reverse_case[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

result = [0 for i in range(n)]
for i in range(n):
    result[i] = increase[i] + decrease[n - i - 1] - 1

print(max(result))