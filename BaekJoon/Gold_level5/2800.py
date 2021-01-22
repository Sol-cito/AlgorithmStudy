import sys
from collections import deque


def recursion(string, arr, sub, idx, res):
    if len(sub) > 0:
        r = ""
        for i in range(len(string)):
            if i not in sub:
                r += string[i]
        if r not in res: res.append(r)
    for i in range(idx, len(arr), 2):
        sub.append(arr[i]), sub.append(arr[i + 1])
        recursion(string, arr, sub, i + 2, res)
        del sub[-1], sub[-1]


string = sys.stdin.readline().rstrip()
que = deque([])
arr = []
for i in range(len(string)):
    if string[i] == '(':
        que.append(i)
    elif string[i] == ')':
        arr.append(que.pop())
        arr.append(i)
res = []
recursion(string, arr, [], 0, res)
res.sort()
[print(ele) for ele in res]
