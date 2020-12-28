import sys
from collections import deque


def bfs(x, y, dic, val, n):
    que = deque([x])
    visit = [0 for _ in range(n)]
    visit[x - 1] = 1
    while que:
        pop = que.pop()
        for ele in dic.get(pop):
            if ele == y:
                return val
            if visit[ele - 1] == 0:
                que.appendleft(ele)
                visit[ele - 1] = 1
    return 0


n, k = map(int, sys.stdin.readline().split(" "))
dic = dict(zip([i for i in range(1, n + 1)], [[] for _ in range(n)]))
for _ in range(k):
    a, b = map(int, sys.stdin.readline().split(" "))
    dic.get(a).append(b)
s = int(sys.stdin.readline())
for _ in range(s):
    a, b = map(int, sys.stdin.readline().split())
    print(bfs(a, b, dic, -1, n) + bfs(b, a, dic, 1, n))
