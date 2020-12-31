import sys
from collections import deque


def check(arr, x, y, visit, directions):
    cnt = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]) and visit[nx][ny] == 0 and arr[nx][ny] <= 0:
            cnt += 1
    arr[x][y] = arr[x][y] - cnt
    return arr[x][y]


def bfs(arr, x, y, directions, visit):
    que = deque([[x, y]])
    while que:
        pop = que.pop()
        check(arr, pop[0], pop[1], visit, directions)
        visit[pop[0]][pop[1]] = 1
        for dx, dy in directions:
            nx, ny = pop[0] + dx, pop[1] + dy
            if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]) and visit[nx][ny] == 0 and arr[nx][ny] > 0:
                que.appendleft([nx, ny])
                visit[nx][ny] = 1


def verify(arr):
    res = 0
    directions = [1, 0], [0, 1], [-1, 0], [0, -1]
    while 1:
        visit = [[0 for _ in range(len(arr[0]))] for _ in range(len(arr))]
        flag, cnt = False, 0
        for i in range(1, len(arr) - 1):
            for j in range(1, len(arr[0]) - 1):
                if arr[i][j] > 0 and visit[i][j] == 0:
                    cnt += 1
                    if flag:
                        return res
                    bfs(arr, i, j, directions, visit)
                    flag = True
        if cnt == 0: break
        res += 1
    return 0


N, M = map(int, sys.stdin.readline().split(" "))
arr = [[int(ele) for ele in sys.stdin.readline().rstrip().split(" ")] for _ in range(N)]
print(verify(arr))