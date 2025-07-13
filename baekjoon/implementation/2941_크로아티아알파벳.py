# https://www.acmicpc.net/problem/2941
# 문제: 크로아티아 알파벳
# 영어 이름: Croatian Alphabet
# 난이도: 실버5
# 분류: 문자열, 구현
# 태그: #string #implementation

import sys

if __name__ == '__main__':
    word: str = sys.stdin.readline().rstrip()
    croatia_letters = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    count = 0
    
    i = len(word) - 1
    while 0 <= i:
        if word[i] in ['=', '-', 'j']:
            if len(word) >= 3 and word[i] == '=':
                if word[i-2:i+1] in ['dz=']:
                    i -= 3
                    count += 1 
                    continue
            if len(word) >= 2 and word[i] == '=':
                if word[i-1:i+1] in ['c=', 's=', 'z=']:
                    i -= 2
                    count += 1
                    continue
            if len(word) >= 2 and word[i] == '-':
                if word[i-1:i+1] in ['c-', 'd-']:
                    i -= 2
                    count += 1
                    continue
            if len(word) >= 2 and word[i] == 'j':
                if word[i-1:i+1] in ['lj', 'nj']:
                    i -= 2
                    count += 1
                    continue
        count += 1
        i -= 1  
    sys.stdout.write(str(count))

    
    