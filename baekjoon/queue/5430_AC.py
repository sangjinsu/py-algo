# https://www.acmicpc.net/problem/5430
# 문제: AC
# 영어 이름: AC
# 난이도: 골드5
# 분류: 구현, 자료구조, 문자열, 파싱
# 태그: #deque #reverse #파싱 #예외처리

import json
import sys
from collections import deque

if __name__ == '__main__':
    readline = sys.stdin.readline
    write = sys.stdout.write

    T = int(readline())
    for _ in range(T):
        process_list = list(readline().rstrip())
        _ = int(readline())
        nums: list[int] = json.loads(readline())
        queue: deque = deque(nums)
        is_reversed = False
        is_error = False

        for process in process_list:
            if process == 'R':
                is_reversed = not is_reversed
            elif process == 'D':
                if queue:
                    if not is_reversed:
                        queue.popleft()
                    else:
                        queue.pop()
                else:
                    is_error = True
                    break

        if is_error:
            write('error\n')
            continue

        if is_reversed:
            queue.reverse()

        write('[{}]\n'.format(','.join(map(str, queue))))