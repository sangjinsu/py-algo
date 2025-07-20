# https://www.acmicpc.net/problem/10986
# 문제: 나머지 합
# 난이도: 골드3
# 분류: 누적 합

import sys

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))

    prefix_sum = 0
    remainder_counts = [0] * m

    for i in range(n):
        prefix_sum += nums[i]
        remainder_counts[prefix_sum % m] += 1

    result = remainder_counts[0]

    for count in remainder_counts:
        result += count * (count - 1) // 2

    print(result)