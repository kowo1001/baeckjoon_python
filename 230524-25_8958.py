
# https://www.acmicpc.net/problem/8958

# 내가 생각한 알고리즘
# 1. 숫자 n을 입력 받는다
# 2. 숫자 n만큼 문자열을 입력받는다
# 3. 각 자리에 연속된 문자가 있으면 +1을 해준다 (단, 각 자리보다 뒤에 자리에 있는 숫자를 더해줄것)
# 4. 각 자리에 연속된 값들을 모두 더해준다
# 5. 출력 끝.

# 내가 생각한 풀이(알고리즘->코드)
n = int(input())

numb = 0

for i in range(n):
    omy = input()
    for j in range(10):
        oxa = input()
        if oxa[j] == oxa[j-1]:
            print(numb+1)
# ㅠㅠ. 쓰레기 코드…


# 다른 사람 풀이
n = int(input())

for _ in range(n):
    ox_list = list(input())
    score = 0
    sum_score = 0
    for ox in ox_list:
        if ox == 'O':
            score += 1
            sum_score += score
        else:
            score = 0
    print(sum_score)
