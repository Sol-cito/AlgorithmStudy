import sys


def isPal(left, right, nums, dp):
    nL, nR = left, right
    while nL < right:
        if dp[nL][nR]: break
        if nums[nL] != nums[nR] or dp[nL][nR] == False:
            dp[nL][nR] = False
            return 0
        nL += 1
        nR -= 1
    while left <= right and dp[left][right] == None:
        dp[left][right] = True
        left += 1
        right -= 1
    return 1


N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split(" ")))
dp = [[None for _ in range(N)] for _ in range(N)]
for _ in range(int(sys.stdin.readline())):
    left, right = map(int, sys.stdin.readline().split(" "))
    print(isPal(left - 1, right - 1, nums, dp))