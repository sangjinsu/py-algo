# https://www.acmicpc.net/problem/1543
# 문제: 문서 검색
# 영어 이름: Document Search
# 난이도: 실버4
# 분류: 문자열, 브루트포스 알고리즘
# 태그: #string #bruteforce

import sys

if __name__ == '__main__':
    readline = sys.stdin.readline
    document = readline().rstrip()
    word = readline().rstrip()
    
    i = 0
    result = 0
    while i < len(document):
        if document[i:i+len(word)] == word:
            i += len(word)
            result += 1
            continue
        i += 1
    print(result)
            
    