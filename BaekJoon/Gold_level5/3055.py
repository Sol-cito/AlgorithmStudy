import sys
from _collections import deque


def waterExpand(starQue, arr):
    nQue = deque([])
    while starQue:
        pop = starQue.pop()
        for x, y in [1, 0], [0, 1], [-1, 0], [0, -1]:
            nx, ny = pop[0] + x, pop[1] + y
            if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]) and (arr[nx][ny] == '.' or arr[nx][ny] == 'S'):
                nQue.appendleft([nx, ny])
                arr[nx][ny] = '*'
    return nQue


def moveS(S, D, arr, res):
    nQue = deque([])
    while S:
        pop = S.pop()
        for x, y in [1, 0], [0, 1], [-1, 0], [0, -1]:
            nx, ny = pop[0] + x, pop[1] + y
            if nx == D[0] and ny == D[1]:
                return nQue, pop[2] + 1
            if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]) and arr[nx][ny] != 'S' and arr[nx][ny] == '.':
                nQue.appendleft([nx, ny, pop[2] + 1])
                arr[nx][ny] = 'S'
    return nQue, res


R, C = map(int, sys.stdin.readline().split(" "))
arr = [list(i for i in sys.stdin.readline().rstrip()) for _ in range(R)]
starQue, D, S = deque([]), [], deque([])
for i in range(R):
    for j in range(C):
        if arr[i][j] == '*':
            starQue.appendleft([i, j])
        elif arr[i][j] == 'D':
            D.append(i)
            D.append(j)
        elif arr[i][j] == 'S':
            S.appendleft([i, j, 0])

res = -1
while S:
    starQue = waterExpand(starQue, arr)
    S, res = moveS(S, D, arr, res)
    if res != -1:
        print(res)
        exit()
print('KAKTUS')
