import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split(" "))
dic = dict(zip([i for i in range(1, N + 1)], [[] for _ in range(N)]))
links = [0 for i in range(N)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split(" "))
    dic.get(a).append(b)
    links[b - 1] += 1
que = deque([])
for i in range(1, N + 1):
    if links[i - 1] == 0:
        links[i - 1] = -1
        que.append(i)
while que:
    pop = que.pop()
    for linkedNode in dic.get(pop):
        links[linkedNode - 1] -= 1
        if links[linkedNode - 1] == 0:
            que.appendleft(linkedNode)
            links[linkedNode - 1] = -1
    print(pop)