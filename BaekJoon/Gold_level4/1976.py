import sys
from collections import deque


def bfs(dic, startNum, set):
    que = deque([startNum])
    while que:
        for ele in dic.get(que.pop()):
            if ele not in set:
                set.add(ele)
                que.append(ele)


N, M = int(sys.stdin.readline()), int(sys.stdin.readline())
dic = dict(zip([i for i in range(1, N + 1)], [[i + 1] for i in range(N)]))
for i in range(1, N + 1):
    arr = list(map(int, sys.stdin.readline().split(" ")))
    for j in range(len(arr)):
        if arr[j] == 1:
            dic.get(i).append(j + 1)
itinerary = list(map(int, sys.stdin.readline().split(" ")))
set = set()
bfs(dic, itinerary[0], set)
for ele in itinerary:
    if ele not in set:
        print("NO")
        exit()
print("YES")
