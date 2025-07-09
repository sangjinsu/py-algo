# https://www.acmicpc.net/problem/10828
# 문제: 스택
# 영어 이름: Stack
# 난이도: 실버4
# 분류: 자료구조, 스택
# 태그: #stack #자료구조기초

import sys


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    readline = sys.stdin.readline
    write = sys.stdout.write
    n = int(readline())

    stack = Stack()
    result = []
    for _ in range(n):
        line = readline().split()
        command = line[0]
        if command == 'push':
            stack.push(int(line[1]))
        elif command == 'pop':
            if stack.empty():
                result.append(-1)
                continue
            result.append(stack.pop())
        elif command == 'size':
            result.append(stack.size())
        elif command == 'empty':
            if stack.empty():
                result.append(1)
                continue
            result.append(0)
        elif command == 'top':
            if stack.empty():
                result.append(-1)
                continue
            result.append(stack.peek())
        else:
            raise ValueError('Invalid command')

    write('\n'.join(map(str, result)))