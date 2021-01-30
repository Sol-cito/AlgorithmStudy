import sys


def binSearch(dp, val):
    left, right = 0, len(dp) - 1
    while left < right:
        mid = (left + right) // 2
        if dp[mid] < val:
            left = mid + 1
        else:
            right = mid
    dp[left] = val


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split(" ")))
dp = [arr[0]]
for i in range(1, len(arr)):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        binSearch(dp, arr[i])
print(len(dp))
