import sys
import heapq


def checkIfPrime(target):
    n = 2
    while n * n <= target:
        if target % n == 0: return False
        n += 1
    return True


N = int(sys.stdin.readline())
heap = ["2", "3", "5", "7"]
for _ in range(N - 1):
    nHeap = []
    while heap:
        target = heapq.heappop(heap)
        for i in range(1, 10):
            if checkIfPrime(int(target + str(i))):
                heapq.heappush(nHeap, target + str(i))
    heap = nHeap
while heap:
    print(heapq.heappop(heap))
