# https://www.acmicpc.net/problem/3079
# 문제: 입국심사
# 영어 이름: Immigration
# 난이도: Gold 5
# 분류: 이분 탐색, 매개 변수 탐색
# 태그: #binary_search #parametric_search

import sys

if __name__ == '__main__':
    readline = sys.stdin.readline
    N, M = map(int, readline().rstrip().split())
    times = [int(readline().rstrip()) for _ in range(N)]

    left = 1
    right = max(times) * M
    answer = right

    while left <= right:
        mid = (left + right) // 2
        
        # mid 시간 동안 처리할 수 있는 사람 수 계산
        people_processed = 0
        for t in times:
            people_processed += mid // t
            # M명을 넘어서면 더 계산할 필요 없음 (오버플로우 방지 및 최적화)
            if people_processed >= M:
                break

        # M명 이상을 처리할 수 있다면, 시간을 줄여본다. (더 최적의 해가 있는지 확인)
        if people_processed >= M:
            answer = mid
            right = mid - 1
        # M명을 처리할 수 없다면, 시간을 늘려야 한다.
        else:
            left = mid + 1
            
    print(answer)

    