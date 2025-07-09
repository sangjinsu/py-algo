# https://www.acmicpc.net/problem/18258
# 문제: 큐 2
# 영어 이름: Queue 2
# 난이도: 실버4
# 분류: 자료구조, 큐
# 태그: #queue #sys_input #deque

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
        if command == 'push':
            queue.append(int(line[1]))
        elif command == 'pop':
            if queue:
                value = queue.popleft()
                result.append(value)
            else:
                result.append(-1)
        elif command == 'size':
            result.append(len(queue))
        elif command == 'empty':
            if queue:
                result.append(0)
            else:
                result.append(1)
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

    write('\n'.join(map(str, result)))