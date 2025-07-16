# https://www.acmicpc.net/problem/1305
# 문제: 광고
# 영어 이름: Advertisement
# 난이도: 플래티넘4
# 분류: 문자열, KMP
# 태그: #string #kmp

def get_pmt(word: str)->list[int] :
    pmt = [0] * len(word)
    j = 0
    for i in range(1, len(word)):
        while j > 0 and word[i] != word[j]:
            j = pmt[j-1]
        if word[i] == word[j]:
            j += 1
        pmt[i] = j
            
    return pmt

if __name__ == '__main__':
    L = int(input().rstrip())
    word = input().rstrip()
    pmt = get_pmt(word)
    print(L - pmt[L-1])