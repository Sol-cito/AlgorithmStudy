import sys


def func(dp, val):
    left, right = 0, len(dp) - 1
    while left < right:
        mid = (left + right) // 2
        if dp[mid] > val:
            right = mid
        else:
            left = mid + 1
    dp[left] = val


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split(" ")))
dp = [arr[0]]
res = 0
for i in range(1, len(arr)):
    if arr[i] >= dp[-1]:
        dp.append(arr[i])
    else:
        func(dp, arr[i])
print(len(arr) - len(dp))