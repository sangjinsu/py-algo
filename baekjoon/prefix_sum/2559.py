# https://www.acmicpc.net/problem/2559
# 문제: 수열
# 난이도: 실버3
# 분류: 누적 합

if __name__ == '__main__':
    N, K = map(int, input().rstrip().split())
    nums = list(map(int, input().rstrip().split()))
    
    window = sum(nums[:K])
    max_num = window 
    
    for i in range(N-K):
        window -= nums[i]
        window += nums[i+K]
        
        if max_num < window:
            max_num = window 
    
    print(max_num)