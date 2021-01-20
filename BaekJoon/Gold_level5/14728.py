import sys

sys.setrecursionlimit(1000000)

N, T = map(int, sys.stdin.readline().split(" "))
arr = []
[arr.append(list(map(int, sys.stdin.readline().split(" ")))) for _ in range(N)]
dp = [0] * (T + 1)
for ele in arr:
    for weight in reversed(range(len(dp))):
        if weight - ele[0] >= 0:
            dp[weight] = max(dp[weight - ele[0]] + ele[1], dp[weight])
        else:
            break
print(dp[-1])
