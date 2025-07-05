# https://www.acmicpc.net/problem/14467
# 문제: 덩치
# 유형 : 구현, 브루트포스

import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    weight_height_list = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

    ranking_list = []


    for i, wh in enumerate(weight_height_list):
        ranking = 1
        for j,wh2 in enumerate(weight_height_list):
            if i == j:
                continue
            if wh[0] < wh2[0] and wh[1] < wh2[1]:
                ranking += 1
        ranking_list.append(ranking)

    sys.stdout.write(' '.join(map(str, ranking_list)))
