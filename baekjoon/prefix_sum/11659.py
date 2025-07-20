# https://www.acmicpc.net/problem/11659
# 문제: 구간 합 구하기 4
# 난이도: 실버3
# 분류: 누적 합

import sys

if __name__ == '__main__':
    readline = sys.stdin.readline
    N, M = map(int, readline().rstrip().split())
    nums = list(map(int, readline().rstrip().split()))
    prefix_sum = [0] * (N+1)
    result = []
    
    for i in range(1, N+1):
        prefix_sum[i] = prefix_sum[i-1] + nums[i-1]
        
    for _ in range(M):
        i, j = map(int, input().rstrip().split())
        result.append((prefix_sum[j] - prefix_sum[i-1]))
    sys.stdout.write('\n'.join(map(str, result)))