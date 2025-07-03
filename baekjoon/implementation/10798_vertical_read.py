# https://www.acmicpc.net/problem/11720
# 문제: 숫자의 합
# 난이도: 브론즈4
# 분류: 구현, 수학
# 태그: #implementation #math #beginner #string
# 풀이: 각 자릿수를 하나씩 더함.

import sys

if __name__ == '__main__':
    _ = int(input())
    numbers = list(map(int, list(input())))

    result = 0
    for number in numbers:
        result += number

    sys.stdout.write(str(result))

