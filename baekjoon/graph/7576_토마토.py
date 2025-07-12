# https://www.acmicpc.net/problem/7576
# 문제: 토마토
# 영어 이름: Tomato
# 난이도: 골드5
# 분류: 그래프 이론, 그래프 탐색, 너비 우선 탐색
# 태그: #bfs #graph_search

import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(mat: list[list[int]], N: int, M: int) -> int:
    queue = deque()
    
    for y in range(N):
        for x in range(M):
            if mat[y][x] == 1:
                queue.append((y, x))
    
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and mat[ny][nx] == 0:
                mat[ny][nx] = mat[y][x] + 1
                queue.append((ny, nx))
    
    max_day = 0
    for y in range(N):
        for x in range(M):
            if mat[y][x] == 0:
                return -1  
            max_day = max(max_day, mat[y][x])
    
    return max_day - 1  

if __name__ == '__main__':
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    M, N = map(int, readline().rstrip().split())
    mat = [list(map(int, readline().rstrip().split())) for _ in range(N)]
    
    result = bfs(mat, N, M)
    write(f'{result}\n')
    
