# https://www.acmicpc.net/problem/1021
# 문제: 회전하는 큐
# 영어 이름: Rotating Queue
# 난이도: 실버3
# 분류: 자료구조, 덱
# 태그: #deque #시뮬레이션

import sys
from collections import deque

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    queue = deque([i for i in range(1, n + 1)])
    nums = list(map(int, sys.stdin.readline().split()))

    result = 0
    for num in nums:
        target = queue.index(num)
        mid = len(queue) // 2
        if target <= mid:
            while queue[0] != num:
                value = queue.popleft()
                queue.append(value)
                result += 1
        else:
            while queue[0] != num:
                value = queue.pop()
                queue.appendleft(value)
                result += 1
        queue.popleft()

    sys.stdout.write(str(result))