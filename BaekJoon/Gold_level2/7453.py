import sys

n = int(sys.stdin.readline())
a, b, c, d = [], [], [], []
for _ in range(n):
    w, x, y, z = map(int, sys.stdin.readline().split(" "))
    a.append(w), b.append(x), c.append(y), d.append(z)
res = 0
dic = {}
for ele1 in a:
    for ele2 in b:
        if ele1 + ele2 in dic:
            dic[ele1 + ele2] += 1
        else:
            dic[ele1 + ele2] = 1
for ele1 in c:
    for ele2 in d:
        if -(ele1 + ele2) in dic:
            res += dic.get(-(ele1 + ele2))
print(res)