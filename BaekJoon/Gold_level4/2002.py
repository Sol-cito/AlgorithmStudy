import sys

n = int(sys.stdin.readline())
carIn = [sys.stdin.readline().rstrip() for _ in range(n)]
dic = dict(zip(carIn, [0 for _ in range(n)]))
res, pointer = 0, 0
for _ in range(n):
    carOut = sys.stdin.readline().rstrip()
    if carIn[pointer] == carOut:
        dic[carOut] = 1
        while pointer < len(carIn) and dic.get(carIn[pointer]) == 1:
            pointer += 1
    else:
        res += 1
        dic[carOut] = 1
print(res)
