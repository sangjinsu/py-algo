# https://www.acmicpc.net/problem/9996
# 문제: 한국이 그리울 땐 서버에 접속하지
# 영어 이름: File Pattern Matching
# 난이도: 실버3
# 분류: 문자열, 구현, 정규 표현식
# 태그: #string #implementation #regex


if __name__ == '__main__':
    N = int(input().rstrip())
    pattern = input().rstrip().split('*')
    pattern_all_len = len(''.join(pattern))
    result = []
    for _ in range(N):
        word = input()
        if len(word) < pattern_all_len:
            result.append('NE')
            continue
        if len(pattern) == 1:
            if pattern[0] == word[:len(pattern[0])]:
                result.append('DA')
                continue
            result.append('NE')
        if len(pattern) == 2:
            if pattern[0] == word[:len(pattern[0])] and pattern[1] == word[(len(word) - len(pattern[1])):]:
                    result.append('DA')
                    continue
            result.append('NE')
    print('\n'.join(result))
            