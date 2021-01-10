import sys, math

a, b = map(int, sys.stdin.readline().split(" "))
z = int(b * 100 / a)
if a == b or z == 99:
    print(-1)
    exit()
print(math.ceil((z * a + a - 100 * b) / (99 - z)))
