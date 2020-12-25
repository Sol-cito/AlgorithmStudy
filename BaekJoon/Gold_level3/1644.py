import sys


def chae(boolArr, primeArr):
    for i in range(2, len(boolArr)):
        if boolArr[i]:
            for j in range(i * 2, len(boolArr), i):
                boolArr[j] = False
            primeArr.append(i)


N = int(sys.stdin.readline())
if N == 1:
    print(0)
    exit()
boolArr = [True for _ in range(N + 1)]
primeArr = []
chae(boolArr, primeArr)
p2, sum, res = 0, primeArr[0], 0
for p1 in range(len(primeArr)):
    while p2 < len(primeArr) and sum + primeArr[p2] < N:
        p2 += 1
        sum += primeArr[p2]
    if sum == N:
        res += 1
    sum -= primeArr[p1]
print(res)