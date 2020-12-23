import sys
from collections import deque


def check(x, y, arr, num):
    res = 0
    for dx, dy in [1, 0], [0, 1], [-1, 0], [0, -1]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]) and arr[nx][ny] == 1:
            arr[nx][ny] = num
            res += 1
    return res


def bfs(arr, num):
    que = deque([[0, 0]])
    arr[0][0] = num
    conversion = 0
    while que:
        pop = que.pop()
        conversion += check(pop[0], pop[1], arr, num)
        for dx, dy in [1, 0], [0, 1], [-1, 0], [0, -1]:
            nx, ny = pop[0] + dx, pop[1] + dy
            if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]) and arr[nx][ny] in (0, num + 1):
                que.appendleft([nx, ny])
                arr[nx][ny] = num
    return conversion


R, C = map(int, sys.stdin.readline().split(" "))
arr = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(R)]
num = -1
res, cnt = 0, 0
while 1:
    conversionNum = bfs(arr, num)
    if conversionNum == 0: break
    num -= 1
    res = conversionNum
    cnt += 1
print(cnt)
print(res)