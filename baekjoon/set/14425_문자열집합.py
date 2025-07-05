# https://www.acmicpc.net/problem/14425
# 문제: 문자열 집합
# 영어 이름: String Set
# 난이도: 실버

if __name__ == '__main__':
    n = int(input())
    str_set = set([input() for _ in range(n)])
    count = 0
    input_str_list = [input() for _ in range(n)]
    for input_str in input_str_list:
        if input_str in str_set:
            count += 1
    print(count)
