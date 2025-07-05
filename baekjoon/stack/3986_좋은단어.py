# https://www.acmicpc.net/problem/3986
# 문제: 좋은 단어
# 영어 이름: Good Word
# 난이도: 실버4

if __name__ == '__main__':
    n = int(input())
    word_list = [input() for _ in range(n)]
    count = 0
    for word in word_list:
        stack = []
        for letter in word:
            if len(stack) == 0:
                stack.append(letter)
                continue
            if letter == stack[-1]:
                stack.pop()
            else:
                stack.append(letter)
        if len(stack) == 0:
            count += 1

    print(count)
