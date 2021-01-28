import sys


def binSearch(dp, val):
    l, r = 0, len(dp) - 1
    while l < r:
        mid = (l + r) // 2
        if dp[mid] > val:
            r = mid
        elif dp[mid] < val:
            l = mid + 1
        else:
            return
    dp[r] = val


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split(" ")))
dp = [arr[0]]
for i in range(1, N):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        binSearch(dp, arr[i])
print(len(dp))
