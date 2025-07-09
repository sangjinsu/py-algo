# https://www.acmicpc.net/problem/2751
# 문제: 수 정렬하기 2
# 영어 이름: Sort Numbers 2
# 난이도: 실버5
# 분류: 정렬
# 태그: #merge_sort #quick_sort #sys_input

import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    result = sorted([int(sys.stdin.readline()) for _ in range(n)])
    sys.stdout.write('\n'.join(map(str, result)))