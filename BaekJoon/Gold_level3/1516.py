import sys


def topDown(dp, dic, timeArr, num):
    if dp[num - 1] != -1:
        return dp[num - 1]
    if not dic.get(num):
        return timeArr.get(num)
    res = dp[num - 1]
    for i in dic.get(num):
        res = max(res, topDown(dp, dic, timeArr, i) + timeArr[num])
    dp[num - 1] = res
    return res


N = int(sys.stdin.readline())
dic = dict(zip([i for i in range(1, N + 1)], [[] for _ in range(N)]))
timeArr = {}
for i in range(N):
    arr = list(map(int, sys.stdin.readline().split(" ")))
    timeArr[i + 1] = arr[0]
    for j in range(1, len(arr) - 1):
        dic.get(i + 1).append(arr[j])
dp = [-1 for _ in range(N)]
for i in range(1, N + 1):
    dp[i - 1] = topDown(dp, dic, timeArr, i)

for i in range(N):
    print(dp[i])
