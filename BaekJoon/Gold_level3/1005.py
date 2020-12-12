import sys
sys.setrecursionlimit(50000000)


def search(dp, val, dic, n):
    # print("노드 번호 : ", n)
    if not dic.get(n + 1):
        return val[n]
    res = 0
    for i in dic.get(n + 1):
        if dp[i - 1] != -1:
            res = max(res, dp[i - 1] + val[n])
        else:
            res = max(res, val[n] + search(dp, val, dic, i - 1))
    dp[n] = res
    return max(dp[n], res)


def testCase():
    N, K = map(int, sys.stdin.readline().rstrip().split(" "))
    val = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    #   점화식 : f(n) = max(f(n), 노드값 + max[f(n)한테 들어오는 a노드들의 f(a)])
    dic = {}
    for _ in range(K):
        a, b = map(int, sys.stdin.readline().rstrip().split(" "))
        if b in dic:
            dic.get(b).append(a)
        else:
            dic[b] = [a]
    dp = [-1 for _ in range(N)]
    target = int(sys.stdin.readline().rstrip())
    return search(dp, val, dic, target - 1)


for i in range(int(sys.stdin.readline().rstrip())):
    sys.stdout.write(str(testCase()) + "\n")
