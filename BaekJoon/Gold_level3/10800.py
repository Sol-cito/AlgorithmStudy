import sys

N = int(sys.stdin.readline().rstrip())
arr, prefix = [], [0] * N
for i in range(1, N + 1):
    a, b = map(int, sys.stdin.readline().split(" "))
    arr.append([b, a, i])
arr.sort()
total, p = 0, arr[0][0]
for i in range(1, len(arr)):
    total += arr[i - 1][0]
    if arr[i][0] != p:
        prefix[i] = total
        p = arr[i][0]
    else:
        prefix[i] = prefix[i - 1]
color = [0] * 200001
res = {}
p2, colorInput = prefix[0], []
for i in range(N):
    if prefix[i] != p2:
        for ele in colorInput:
            color[ele[0] - 1] += ele[1]
        colorInput = []
        p2 = prefix[i]
    res[arr[i][2]] = prefix[i] - color[arr[i][1] - 1]
    colorInput.append([arr[i][1], arr[i][0]])
[print(res.get(i)) for i in range(1, N + 1)]
