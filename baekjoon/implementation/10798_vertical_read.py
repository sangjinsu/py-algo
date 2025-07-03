# https://www.acmicpc.net/problem/11720
# 문제: 세로 읽기
if __name__ == '__main__':
    row = 5
    wordList = [input() for _ in range(row)]
    maxLen = max(map(len, wordList))

    result = ""
    for x in range(maxLen):
        for y in range(row):
            if len(wordList[y]) <= x:
                continue
            result += wordList[y][x]

    print(result)
