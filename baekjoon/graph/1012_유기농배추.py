# https://www.acmicpc.net/problem/1012
# 문제: 유기농 배추
# 영어 이름: Organic Cabbage
# 난이도: 실버2
# 분류: 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
# 태그: #bfs #dfs #graph_search

import sys 

dx = [0, 0 , -1, 1]
dy = [-1, 1, 0, 0]

def dfs(graph, visited, M, N, y, x):
    stack = [(x, y)]
    visited[y][x] = True
    
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                stack.append((nx, ny))

if __name__ == '__main__':
    readline = sys.stdin.readline
    write = sys.stdout.write
    t = int(readline())
    
    for _ in range(t):
        M, N, K = map(int, readline().split())
        graph = [[0] * M for _ in range(N)]
        visited = [[False] * M for _ in range(N)]


        for _ in range(K):
            x, y = map(int, readline().split())
            graph[y][x] = 1
        
        count = 0
        for y in range(N):
            for x in range(M):
                if graph[y][x] == 1 and not visited[y][x]:
                    dfs(graph, visited, M, N, y, x)
                    count += 1
        
        write(str(count) + '\n')
    
    

