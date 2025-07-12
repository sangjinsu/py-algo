# https://www.acmicpc.net/problem/1697
# 문제: 숨바꼭질
# 영어 이름: Hide-and-seek
# 난이도: 실버1
# 분류: 그래프 이론, 그래프 탐색, 너비 우선 탐색
# 태그: #bfs #graph_search

import sys
from collections import deque

MAX = 100001

def bfs(N, K):
    if N >= K:
        return N - K

    queue = deque([(N, 0)])
    visited = [False] * MAX
    visited[N] = True
    
    while queue:
        current, time = queue.popleft()
        
        if current == K:
            return time
        
        for next_pos in [current - 1, current + 1, current * 2]:
            if 0 <= next_pos < MAX and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, time + 1))

if __name__ == '__main__':
    readline = sys.stdin.readline
    N, K = map(int, readline().split())
    
    sys.stdout.write(str(bfs(N, K)) + '\n')