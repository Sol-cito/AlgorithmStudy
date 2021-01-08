import sys

N, K = map(int, sys.stdin.readline().rstrip().split(" "))
names = [len(sys.stdin.readline().rstrip()) for _ in range(N)]
arr = [0] * 21
p2 = res = 0
for p1 in range(N - K):
    while p2 < len(names) and p2 - p1 <= K:
        arr[names[p2]] += 1
        if arr[names[p2]] > 1: res += arr[names[p2]] - 1
        p2 += 1
    arr[names[p1]] -= 1
print(res)
