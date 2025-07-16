# https://www.acmicpc.net/problem/12891
# 문제: DNA 비밀번호
# 영어 이름: DNA Password
# 난이도: 실버2
# 분류: 문자열, 슬라이딩 윈도우
# 태그: #string #sliding_window

import sys

def check(current, required):
    for key in required:
        if current[key] < required[key]:
            return False
    return True

if __name__ == '__main__':
    readline = sys.stdin.readline
    
    S, P = map(int, readline().rstrip().split())
    DNA = readline().rstrip()
    min_counts = list(map(int, readline().rstrip().split()))
    
    required = {'A': min_counts[0], 'C': min_counts[1], 'G': min_counts[2], 'T': min_counts[3]}
    current = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    
    result = 0
    
    for i in range(P):
        current[DNA[i]] += 1
        
    if check(current, required):
        result += 1
        
    # 슬라이딩 윈도우
    for i in range(P, S):
        left_char = DNA[i - P]
        current[left_char] -= 1
        
        right_char = DNA[i]
        current[right_char] += 1
        
        if check(current, required):
            result += 1
            
    print(result)
