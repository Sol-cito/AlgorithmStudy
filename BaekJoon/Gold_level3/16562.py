import sys
from _collections import deque


def bfs(friendsCost, nodes, startNode, visit):
    que = deque([startNode])
    visit[startNode - 1] = 1
    res = 10000000
    while que:
        pop = que.pop()
        res = min(res, friendsCost.get(pop))
        for i in nodes.get(pop):
            if visit[i - 1] == 0:
                visit[i - 1] = 1
                que.appendleft(i)
    return res


N, M, k = map(int, sys.stdin.readline().split(" "))
friendsCost = dict(zip([i for i in range(1, N + 1)], list(map(int, sys.stdin.readline().split(" ")))))
nodes = dict(zip([i for i in range(1, N + 1)], [[] for _ in range(N)]))
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split(" "))
    nodes.get(a).append(b)
    nodes.get(b).append(a)
visit = [0 for _ in range(N)]
res = 0
for i in range(1, N + 1):
    if visit[i - 1] == 0:
        res += bfs(friendsCost, nodes, i, visit)
        if res > k:
            print("Oh no")
            exit()
print(res)
