# https://www.acmicpc.net/problem/1260
# 문제: DFS와 BFS
# 영어 이름: DFS and BFS
# 난이도: 실버2
# 분류: 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
# 태그: #bfs #dfs #graph #adjacency_list

import sys
from collections import deque, defaultdict


def dfs(graph, start_node):
    visited = []
    visited_set = set()
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited_set:
            visited_set.add(node)
            visited.append(node)
            stack.extend(reversed(graph.get(node, [])))
    return visited


def bfs(graph, start_node):
    visited = []
    visited_set = {start_node}
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        visited.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited_set:
                visited_set.add(neighbor)
                queue.append(neighbor)
    return visited


if __name__ == '__main__':
    input = sys.stdin.readline
    n, m, v = map(int, input().split())

    graph = defaultdict(list)
    for _ in range(m):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    for key in graph:
        graph[key].sort()

    dfs_result = dfs(graph, v)
    print(*dfs_result)

    bfs_result = bfs(graph, v)
    print(*bfs_result)
