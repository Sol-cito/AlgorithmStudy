import sys

N, d, k, c = map(int, sys.stdin.readline().split(" "))
arr = [int(sys.stdin.readline()) for _ in range(N)]
for i in arr[:k - 1]: arr.append(i)
p2, res, ans = 0, 1, 1
chobap = [0 for _ in range(d)]
chobap[arr[0] - 1] = 1
for p1 in range(len(arr) - k):
    while p2 - p1 < k - 1 and p2 < len(arr) - 1:
        p2 += 1
        if chobap[arr[p2] - 1] == 0:
            res += 1
        chobap[arr[p2] - 1] += 1
        if chobap[c - 1] == 0:
            ans = max(ans, res + 1)
        else:
            ans = max(ans, res)
    chobap[arr[p1] - 1] -= 1
    if chobap[arr[p1] - 1] == 0:
        res -= 1
print(ans)
