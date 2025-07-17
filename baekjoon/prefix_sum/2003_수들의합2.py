# https://www.acmicpc.net/problem/2003
# 문제: 수들의 합 2
# 난이도: 실버4
# 분류: 누적 합, 두 포인터

import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().rstrip().split())
    nums = list(map(int, sys.stdin.readline().rstrip().split()))

    count = 0
    start = 0
    end = 0
    current_sum = 0

    while True:
        if current_sum >= M:
            if current_sum == M:
                count += 1
            current_sum -= nums[start]
            start += 1
        elif end == N:
            break
        else:
            current_sum += nums[end]
            end += 1
            
    print(count)
