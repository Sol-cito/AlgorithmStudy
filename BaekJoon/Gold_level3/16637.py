import sys


def cal(a, op, b):
    if op == '+':
        return int(a) + int(b)
    elif op == '-':
        return int(a) - int(b)
    else:
        return int(a) * int(b)


def recursion(sik, res, visit):
    for i in range(0, len(sik) - 1, 2):
        if visit[i] == 1 or visit[i + 2] == 1: continue
        nSik = []
        nSik.extend(sik[:i])
        nSik.extend([cal(sik[i], sik[i + 1], sik[i + 2])])
        nSik.extend(sik[i + 3:])
        visit[i] = 1
        del visit[i + 1]
        del visit[i + 1]
        res = max(res, recursion(nSik, res, visit))
        visit[i] = 0
        visit.insert(i + 1, 0)
        visit.insert(i + 1, 0)
    while len(sik) > 1:
        sik[2] = cal(sik[0], sik[1], sik[2])
        sik = sik[2:]
    res = max(res, sik[0])
    return res


N = int(sys.stdin.readline().rstrip())
sik = list(str(sys.stdin.readline()).rstrip())
if N == 1:
    print(int(sik[0]))
    exit()
res = - 2147483648
visit = [0 for _ in range(N)]
res = max(res, recursion(sik, res, visit))
print(res)
