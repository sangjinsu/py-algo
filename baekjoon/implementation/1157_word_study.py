# https://www.acmicpc.net/problem/1157
# 문제: 단어 공부
import sys


def solve(word: str) -> str:
    letter_count = {}

    for letter in word:
        letter_count[letter] = letter_count.get(letter, 0) + 1

    result = []
    max_letter_count = max(letter_count.values())
    for letter, count in letter_count.items():
        if count == max_letter_count:
            result.append(letter)

    if len(result) > 1:
        return '?'

    return result[0].upper()


if __name__ == '__main__':
    word = sys.stdin.readline().strip().lower()
    result = solve(word)
    sys.stdout.write(result)
