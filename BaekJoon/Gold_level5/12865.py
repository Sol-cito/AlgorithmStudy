import sys

N, K = map(int, sys.stdin.readline().split(" "))
arr = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split(" "))
    arr.append([a, b])
dp = [0] * (K + 1)
for stuff in arr:
    for i in reversed(range(len(dp))):
        if i - stuff[0] >= 0:
            dp[i] = (max(dp[i - stuff[0]] + stuff[1], dp[i]))
print(dp[-1])