import sys

sys.setrecursionlimit(100000000)


def dfs(arr, x, y, dp, directions):
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    for dir in directions:
        nx, ny = x + dir[0], y + dir[1]
        if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]) and arr[nx][ny] > arr[x][y]:
            dp[x][y] += dfs(arr, nx, ny, dp, directions)
    return dp[x][y]


M, N = map(int, sys.stdin.readline().split(" "))
arr = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(M)]
dp = [[-1 for _ in range(N)] for _ in range(M)]
dp[0][0] = 1
directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
print(dfs(arr, M - 1, N - 1, dp, directions))