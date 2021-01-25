import sys

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]
if len(arr) == 1:
    print(arr[0])
    exit()
arr.sort()
dp = [0] * N
dp[0] = arr[0]
dp[1] = max(arr[0] + arr[1], arr[0] * arr[1])
for i in range(2, N):
    dp[i] = max(dp[i - 1] + arr[i], dp[i - 2] + arr[i - 1] * arr[i])
print(dp[-1])
