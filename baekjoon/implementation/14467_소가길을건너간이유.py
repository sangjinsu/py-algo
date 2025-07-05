# https://www.acmicpc.net/problem/14467
# 문제: 소가 길을 건너간 이유
# 유형 : 구현

import sys

if __name__ == '__main__':
    readline = sys.stdin.readline
    N = int(readline())
    cross = dict()
    result = 0
    for _ in range(N):
        cow, side = map(int, readline().split())
        if cross.get(cow) is None:
            cross[cow] = side
        else:
            if cross[cow] != side:
                cross[cow] = side
                result += 1

    sys.stdout.write(str(result))
