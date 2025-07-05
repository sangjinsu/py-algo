# https://www.acmicpc.net/problem/1620
# 문제: 나는야 포켓몬 마스터 이다솜
# 영어 이름: I’m a Pokémon Master (Idasom)
# 난이도: 실버4

if __name__ == '__main__':
    n, m = map(int, input().split())

    dogam_name_to_number = dict()
    dogam_number_to_name = ['']
    for i in range(1, n + 1):
        name = input().rstrip()
        dogam_name_to_number[name] = i
        dogam_number_to_name.append(name)

    result = []
    for _ in range(m):
        question = input().rstrip()
        if question.isalpha():
            result.append(dogam_name_to_number[question])
        if question.isdigit():
            result.append(dogam_number_to_name[int(question)])

    for item in result:
        print(item)
