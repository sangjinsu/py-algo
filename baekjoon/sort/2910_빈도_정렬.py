# https://www.acmicpc.net/problem/2910
# 문제: 빈도 정렬
# 영어 이름: Frequency Sort
# 난이도: 실버3
# 분류: 정렬, 해시
# 태그: #sorting #frequency #hashmap #stable_sort


if __name__ == '__main__':
    n, c = map(int, input().split())
    nums = list(map(int, input().split()))

    freq = dict()
    order = dict()

    for i, num in enumerate(nums):
        freq[num] = freq.get(num, 0) + 1
        if num not in order:
            order[num] = i

    vectors = [(num, freq[num], order[num]) for num in freq]
    vectors.sort(key=lambda x: (-x[1], x[2]))

    result = [num for num, f, _ in vectors for _ in range(f)]
    print(' '.join(map(str, result)))
