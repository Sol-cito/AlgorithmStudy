import sys

N, D = map(int, sys.stdin.readline().split(" "))
set = set([0, D])
shortcuts = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
arr, dp = [0, D], [i for i in range(10000)]
for ele in shortcuts:
    if ele[0] not in set:
        arr.append(ele[0])
        set.add(ele[0])
    if ele[1] not in set:
        arr.append(ele[1])
        set.add(ele[1])
arr.sort()
res = 0
for i in range(1, len(arr)):
    dp[arr[i]] = dp[arr[i - 1]] + arr[i] - arr[i - 1]  # 이 값은 안변함
    for cut in shortcuts:
        if arr[i] == cut[1]:
            dp[arr[i]] = min(dp[arr[i]],
                             dp[cut[0]] + cut[2])  # 얘가 여기서 dp[i - 1]이 아니라 cut[2]만큼 뺀 구간의 값과 비교해야 함.
    if arr[i] == D: res = dp[arr[i]]
print(res)
