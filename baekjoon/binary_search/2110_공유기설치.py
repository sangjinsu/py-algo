# https://www.acmicpc.net/problem/2110
# 문제: 공유기 설치
# 난이도: 골드5
# 분류: 이진 탐색
import sys

if __name__ == '__main__':
    N, C = map(int, sys.stdin.readline().rstrip().split())
    homes = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
    homes.sort()

    start = 1
    end = homes[-1] - homes[0]
    result = 0

    while start <= end:
        mid = (start + end) // 2

        count = 1
        last_installed_pos = homes[0]
        for i in range(1, N):
            if homes[i] - last_installed_pos >= mid:
                count += 1
                last_installed_pos = homes[i]

        if count >= C:
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    print(result)
        

        