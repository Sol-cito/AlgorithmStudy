import sys
from collections import deque


def check(arr, x, y):
    cnt = 0
    for dx, dy in [1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]:
        if arr[x + dx][y + dy] == '.': cnt += 1
    arr[x][y] -= cnt
    return arr[x][y]


R, C = map(int, sys.stdin.readline().split(" "))
arr = [[int(i) if i != '.' else i for i in sys.stdin.readline().rstrip()] for _ in range(R)]
que = deque([])
for i in range(1, R - 1):
    for j in range(1, C - 1):
        if arr[i][j] != '.' and check(arr, i, j) <= 0: que.appendleft([i, j])
res = 0
while que:
    nQue = deque([])
    while que:
        pop = que.pop()
        for dx, dy in [1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]:
            if arr[pop[0] + dx][pop[1] + dy] != '.': arr[pop[0] + dx][pop[1] + dy] -= 1
            if arr[pop[0] + dx][pop[1] + dy] == 0:
                nQue.appendleft([pop[0] + dx, pop[1] + dy])
    res += 1
    que = nQue
print(res)
