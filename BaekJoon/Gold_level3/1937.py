import sys

sys.setrecursionlimit(1000000)


def topdown(arr, dp, i, j):
    val = 1
    for dx, dy in [1, 0], [0, 1], [-1, 0], [0, -1]:
        nx, ny = i + dx, j + dy
        if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]) and arr[i][j] > arr[nx][ny]:
            if dp[nx][ny] == -1:
                val = max(val, topdown(arr, dp, nx, ny) + 1)
            else:
                val = max(val, dp[nx][ny] + 1)
    dp[i][j] = val
    return dp[i][j]


n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(n)]
res = 0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if dp[i][j] == -1:
            res = max(res, topdown(arr, dp, i, j))
        else:
            res = max(res, dp[i][j])
print(res)
