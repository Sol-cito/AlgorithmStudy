import sys


def recursion(x, y, arr, visit, dp, num):
    if dp[x][y] != 0:
        return dp[x][y]
    if visit[x][y] == 1:
        return num
    if 0 <= x + 1 < len(arr) and arr[x][y] == 'D':
        visit[x][y] = 1
        dp[x][y] = recursion(x + 1, y, arr, visit, dp, num)
    elif 0 <= x - 1 < len(arr) and arr[x][y] == 'U':
        visit[x][y] = 1
        dp[x][y] = recursion(x - 1, y, arr, visit, dp, num)
    elif 0 <= y + 1 < len(arr[0]) and arr[x][y] == 'R':
        visit[x][y] = 1
        dp[x][y] = recursion(x, y + 1, arr, visit, dp, num)
    elif 0 <= y - 1 < len(arr[0]) and arr[x][y] == 'L':
        visit[x][y] = 1
        dp[x][y] = recursion(x, y - 1, arr, visit, dp, num)
    return dp[x][y]


N, M = map(int, sys.stdin.readline().split(" "))
arr = [[i for i in sys.stdin.readline().rstrip()] for _ in range(N)]
visit = [[0] * M for _ in range(N)]
dp = [[0] * M for _ in range(N)]
num = 1
set = set()
for i in range(N):
    for j in range(M):
        if visit[i][j] == 0:
            set.add(recursion(i, j, arr, visit, dp, num))
            num += 1
print(len(set))