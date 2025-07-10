# https://www.acmicpc.net/problem/11650
# 문제: 좌표 정렬하기
# 영어 이름: Sort Coordinates
# 난이도: 실버5
# 분류: 정렬
# 태그: #튜플정렬 #lambda #2차원정렬

import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    points.sort()
    output = '\n'.join(f'{p[0]} {p[1]}' for p in points)
    sys.stdout.write(output + '\n')
