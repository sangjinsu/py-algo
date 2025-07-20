# https://www.acmicpc.net/problem/2143
# 문제: 두 배열의 합
# 난이도: 골드3
# 분류: 누적 합

from collections import defaultdict
import sys

if __name__ == '__main__':
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    T = int(readline().rstrip())
    n = int(readline().rstrip())
    a_nums = list(map(int, readline().rstrip().split()))
    m = int(readline().rstrip())
    b_nums = list(map(int, readline().rstrip().split()))
    
    a_prefix_sum = defaultdict(int)
    b_prefix_sum = defaultdict(int)
    
    for i in range(n):
        prefix = 0
        for j in range(i, n):
            prefix += a_nums[j]
            a_prefix_sum[prefix] += 1 
            
    for i in range(m):   
        prefix = 0
        for j in range(i, m):
            prefix += b_nums[j]
            b_prefix_sum[prefix] += 1 
    
    result = 0
    for a in a_prefix_sum:
        value = T - a 
        if value in b_prefix_sum:
            result += a_prefix_sum[a] * b_prefix_sum[value]
    
    write(str(result) + '\n')
                
        
        
    