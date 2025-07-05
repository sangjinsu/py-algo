# https://www.acmicpc.net/problem/14467
# 문제: 전구
# 유형 : 구현

import sys


def command1(i, x, bulb_list) -> list[int]:
    new_bulb_list = bulb_list[:]
    new_bulb_list[i - 1] = x
    return new_bulb_list


def command2(l, r, bulb_list) -> list[int]:
    new_bulb_list = bulb_list[:]
    for i in range(l - 1, r):
        if new_bulb_list[i] == 0:
            new_bulb_list[i] = 1
        elif new_bulb_list[i] == 1:
            new_bulb_list[i] = 0
    return new_bulb_list


def command3(l, r, bulb_list) -> list[int]:
    new_bulb_list = bulb_list[:]
    for i in range(l - 1, r):
        new_bulb_list[i] = 0
    return new_bulb_list


def command4(l, r, bulb_list) -> list[int]:
    new_bulb_list = bulb_list[:]
    for i in range(l - 1, r):
        new_bulb_list[i] = 1
    return new_bulb_list


if __name__ == '__main__':
    readline = sys.stdin.readline
    writer = sys.stdout.write

    N, M = map(int, readline().split())
    bulb_list = list(map(int, readline().split()))
    for _ in range(M):

        [command, cond1, cond2] = map(int, readline().split())
        if command == 1:
            bulb_list = command1(cond1, cond2, bulb_list)
        if command == 2:
            bulb_list = command2(cond1, cond2, bulb_list)
        if command == 3:
            bulb_list = command3(cond1, cond2, bulb_list)
        if command == 4:
            bulb_list = command4(cond1, cond2, bulb_list)
    writer(" ".join(map(str, bulb_list)))