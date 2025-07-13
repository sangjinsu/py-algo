# https://www.acmicpc.net/problem/1920
# 문제: 수 찾기
# 영어 이름: Finding a Number
# 난이도: 실버4
# 분류: 이분 탐색, 정렬
# 태그: #binary_search #sort

import sys

if __name__ == '__main__':
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    _ = readline()
    fivots = set(readline().rstrip().split())
        
    _ = readline()
    nums: list[str] = readline().rstrip().split()
    for num in nums:
        if num in fivots:
            write('1\n')
            continue
        write('0\n')