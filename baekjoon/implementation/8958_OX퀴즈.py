# https://www.acmicpc.net/problem/8958
# 문제: OX퀴즈
# 영어 이름: OX Quiz
# 난이도: 브론즈2
# 분류: 문자열, 구현
# 태그: #string #implementation

import sys

def count_score(answer : str) -> int :
    score = 0
    o_list = answer.split('X')
    for o in o_list:
        if len(o) <= 0 :
            continue
        for i in range(1, len(o) + 1):
            score += i
    return score

if __name__ == '__main__':
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    test_case = int(readline())
    for _ in range(test_case):
        answer = readline().rstrip()
        result = count_score(answer)
        write(str(result) + '\n')