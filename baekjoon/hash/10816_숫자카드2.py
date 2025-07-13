# https://www.acmicpc.net/problem/10816
# 문제: 숫자 카드 2
# 영어 이름: Number Card 2
# 난이도: 실버4
# 분류: 해시를 사용한 집합과 맵, 자료 구조, 정렬, 이분 탐색
# 태그: #hash_map #data_structures

import sys
from collections import Counter

if __name__ == '__main__':
    readline = sys.stdin.readline
    
    _ = readline()
    counts = Counter(readline().rstrip().split())
    
    _ = readline()
    cards = readline().rstrip().split()
    
    result = [str(counts.get(card, 0)) for card in cards]
    
    print(' '.join(result))
    