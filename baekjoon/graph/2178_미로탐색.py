# https://www.acmicpc.net/problem/2178
# 문제: 미로 탐색
# 영어 이름: Maze Search
# 난이도: 실버1
# 분류: 그래프 이론, 그래프 탐색, 너비 우선 탐색
# 태그: #bfs #graph_search

import sys 
from collections import deque

# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
    
def bfs(mat, checked, n, m):
    queue = deque([(0, 0)])
    checked[0][0] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] == 1 and not checked[nx][ny]:
                checked[nx][ny] = checked[x][y] + 1
                queue.append((nx, ny))
                
    
    return checked[n-1][m-1]

if __name__ == '__main__':
    readline = sys.stdin.readline
    n, m = map(int, readline().split())
    mat = [list(map(int, readline().strip())) for _ in range(n)]
    checked = [[False] * m for _ in range(n)]

    sys.stdout.write(str(bfs(mat, checked, n, m)))

   
    

    
