import sys
from _collections import deque


def bfs(arr, visit):
    que = deque([[0, 0, 0]])
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    arr[0][0] = 1
    while que:
        pop = que.pop()
        for dir in directions:
            nx, ny = pop[0] + dir[0], pop[1] + dir[1]
            if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]) and arr[nx][ny] == 0:
                arr[nx][ny] = 1
                visit[nx][ny] = pop[2] + 1
                que.appendleft([nx, ny, pop[2] + 1])


# def moveKnight(arr, visit, K):

K = int(sys.stdin.readline())
C, R = map(int, sys.stdin.readline().split(" "))
arr = [list(map(int, sys.stdin.readline().split(" "))) for i in range(R)]
visit = [[0] * C for i in range(R)]
bfs(arr, visit)
print(arr)
print(visit)
# moveKnight(arr, visit, K)
