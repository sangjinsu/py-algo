# https://www.acmicpc.net/problem/10866
# 문제: 덱
# 영어 이름: Deque
# 난이도: 실버4
# 분류: 자료구조, 덱
# 태그: #deque #자료구조기초

import sys
from collections import deque

if __name__ == '__main__':
    readline = sys.stdin.readline
    write = sys.stdout.write

    n = int(readline())
    queue = deque()
    result = []
    for _ in range(n):
        line = readline().rstrip().split()
        command = line[0]
        if command == 'push_front':
            value = int(line[1])
            queue.appendleft(value)
        elif command == 'pop_front':
            if queue:
                value = queue.popleft()
                result.append(value)
            else:
                result.append(-1)
        elif command == 'push_back':
            value = int(line[1])
            queue.append(value)
        elif command == 'pop_back':
            if queue:
                value = queue.pop()
                result.append(value)
            else:
                result.append(-1)
        elif command == 'front':
            if queue:
                result.append(queue[0])
            else:
                result.append(-1)
        elif command == 'back':
            if queue:
                result.append(queue[-1])
            else:
                result.append(-1)
        elif command == 'size':
            result.append(len(queue))
        elif command == 'empty':
            if queue:
                result.append(0)
            else:
                result.append(1)
        else:
            raise ValueError('Invalid command')

    sys.stdout.write('\n'.join(map(str, result)))