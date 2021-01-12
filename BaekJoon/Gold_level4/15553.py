import sys

N, K = map(int, sys.stdin.readline().split(" "))
arr = [int(sys.stdin.readline())]
gap = []
for _ in range(N - 1):
    input = int(sys.stdin.readline())
    gap.append(input - (arr[-1] + 1)) if arr[-1] + 1 < input else gap
    arr.append(input)
gap.sort(reverse=True)
print(arr[-1] + 1 - arr[0] - sum(gap[:K - 1]))
