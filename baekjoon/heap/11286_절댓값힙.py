# https://www.acmicpc.net/problem/11286
# 문제: 절댓값 힙
# 영어 이름: Absolute Heap
# 난이도: 실버1
# 분류: 자료 구조, 우선순위 큐
# 태그: #heap #priority_queue

import heapq
import sys

if __name__ == '__main__':
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N = int(readline())
    hq = []
    result = []
    for _ in range(N):
        v = int(readline())
        if v == 0:
            if not hq:
                write('0\n')
                continue
            
            value = heapq.heappop(hq)
            write(str(value[1]) + '\n')
            continue 
        heapq.heappush(hq, (abs(v), v))
    