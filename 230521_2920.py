# 23년 5월 23일 1일 1백준 기록(2920)

# https://www.acmicpc.net/problem/2920

# 내가 생각한 알고리즘
# 1. 1부터 8까지 오름차순으로 순서대로 커지면 ascending 
# 2. 8부터 1까지 내림차순으로 순서대로 작아지면 descending
# 3. 그 외 나머지는 mixed

# 내가 생각한 풀이 (알고리즘 -> 코드)

a = input().split()

if  a[0] == 1 && a[1] == 2:
    print(‘ascending’)
elif a[1] == 2 && a[0] == 1:
    print(‘descending’)
else:
    print(‘mixed’)


# 다른 사람 풀이
scale = list(map(int, input().split()))

if scale == sorted(scale):
    print("ascending")
elif scale == sorted(scale, reverse = True):
    print("descending")
else:
    print("mixed")




