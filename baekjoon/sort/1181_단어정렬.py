# https://www.acmicpc.net/problem/1181
# 문제: 단어 정렬
# 영어 이름: Word Sort
# 난이도: 실버5
# 분류: 정렬, 문자열
# 태그: #문자열정렬 #길이우선정렬 #사전순정렬

import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())

    word_set = {sys.stdin.readline().rstrip() for _ in range(n)}

    word_list = sorted(word_set, key=lambda w: (len(w), w))
    sys.stdout.write("\n".join(word_list))