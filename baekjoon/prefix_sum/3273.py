# https://www.acmicpc.net/problem/3273
# 문제: 두 수의 합
# 난이도: 실버3
# 분류: 누적 합

from collections import defaultdict

if __name__ == '__main__':
    n = int(input().rstrip())
    nums = list(map(int, input().rstrip().split()))
    x = int(input().rstrip())
    
    exist_checker = defaultdict(int)
    for i, num in enumerate(nums):
        exist_checker[num] = i
    
    result = 0
    for i, num in enumerate(nums):
        target = x - num 
        idx = exist_checker.get(target, -1)
        if idx == -1 or idx <= i:
            continue 
        else:
            result += 1 
            
    print(result)
        