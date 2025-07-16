# https://www.acmicpc.net/problem/11656
# 문제: 접미사 배열
# 영어 이름: Suffix Array
# 난이도: 실버4
# 분류: 문자열, 정렬
# 태그: #string #sorting

if __name__ == '__main__':
    word = input().rstrip()
    suffix_list = list()
    for i in range(len(word)):
        suffix_list.append(word[i:])
    suffix_list.sort()
    print('\n'.join(suffix_list))