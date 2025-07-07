# https://www.acmicpc.net/problem/11279
# 문제: 최대힙
# 영어 이름: Max Heap
# 난이도: 실버2
# 분류: 자료구조, 힙
# 태그: #heap #priority_queue #maxheap #custom_heap

import heapq
import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())

    heap = []
    nums = []
    for _ in range(n):
        num = int(sys.stdin.readline())
        nums.append((-num, num))

    for num in nums:
        if num[1] != 0:
            heapq.heappush(heap, num)
            continue
        if not heap:
            sys.stdout.write('0\n')
            continue
        value = heapq.heappop(heap)
        sys.stdout.write(str(value[1]) + '\n')