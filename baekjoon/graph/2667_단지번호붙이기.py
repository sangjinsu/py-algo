# https://www.acmicpc.net/problem/2667
# 문제: 단지번호붙이기
# 영어 이름: Numbering Complexes
# 난이도: 실버1
# 분류: 그래프 이론, 그래프 탐색, 너비 우선 탐각, 깊이 우선 탐색
# 태그: #bfs #dfs #graph_search

import sys 

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(mat, checked, y, x, N, address):
    stack = [(y, x)]
    checked[y][x] = address
    count = 1

    while stack:
        y, x = stack.pop()
        for i in range(4):
            nx = x + dx[i]  
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N and mat[ny][nx] == 1 and checked[ny][nx] == 0:
                stack.append((ny, nx))
                checked[ny][nx] = address
                count += 1
    return count

if __name__ == '__main__':
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N = int(readline())
    mat = [list(map(int, readline().strip())) for _ in range(N)]
    checked = [[0] * N for _ in range(N)]
    
    address = 1
    address_cnt_list = []
    for y in range(N):
        for x in range(N):
            if mat[y][x] == 1 and checked[y][x] == 0:
                address_cnt = dfs(mat, checked, y, x, N, address)
                address_cnt_list.append(address_cnt)
                address += 1
    
    # 결과 정렬
    address_cnt_list.sort()
    
    write(str(len(address_cnt_list)) + '\n')
    for address_cnt in address_cnt_list:
        write(str(address_cnt) + '\n')
    