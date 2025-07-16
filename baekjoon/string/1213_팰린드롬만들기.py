# https://www.acmicpc.net/problem/1213
# 문제: 팰린드롬 만들기
# 영어 이름: Make a Palindrome
# 난이도: 실버3
# 분류: 문자열, 그리디 알고리즘, 구현
# 태그: #string #greedy #implementation

import sys
from collections import Counter

if __name__ == '__main__':
    name = sys.stdin.readline().strip()
    counts = Counter(name)
    
    odd_chars = [char for char, count in counts.items() if count % 2 != 0]
    
    if len(odd_chars) > 1:
        print("I'm Sorry Hansoo")
    else:
        first_half = ""
        for char_code in range(ord('A'), ord('Z') + 1):
            char = chr(char_code)
            first_half += char * (counts[char] // 2)
            
        middle_char = ""
        if odd_chars:
            middle_char = odd_chars[0]
            
        second_half = first_half[::-1]
        
        result = first_half + middle_char + second_half
        print(result)


    
    
    