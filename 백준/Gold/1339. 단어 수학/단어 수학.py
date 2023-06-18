from string import ascii_uppercase

n = int(input())
arr = []
alpha = {x:[] for x in ascii_uppercase}

for _ in range(n):
    s = input()
    for i in range(len(s)): alpha[s[i]].append(len(s) - 1 - i)

answer = 0
val = 9
for k,v in sorted(alpha.items(), key=lambda x: sum(10 ** a * val for a in x[1]), reverse=True):
    answer += sum(10 ** x * val for x in v)
    val -= 1

print(answer)