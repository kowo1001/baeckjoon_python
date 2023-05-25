# 23년 5월 22일 1일 1백준 기록(2675)

# https://www.acmicpc.net/problem/2675

# 1일 1백준은 아침 일찍 풀어야 하게 된다. 저녁에 죽어도 안풀음.

# 내가 생각한 알고리즘
# 1. 숫자 n을 입력받는다
# 2. 또 숫자 m을 입력 받고 띄어쓰기로 구분해서 숫자와, 알파벳 문자열을 받는다
# 3. 각 문자를 배열에 넣어준다
# 4. 각각의 알파벳 문자를 숫자 m만큼 반복을 해서 출력해준다
# 5. 전체적으로 n만큼 2~4번을 반복해준다

# 첫번째 풀이(알고리즘을->코드로 변환)
n = int(input())

m, arr[] = input().split('')

num = int(m)

for i in range(n):
    print('\n')
    for j in range(num):
        print(arr[j] * num)


# 다른 사람 풀이
t = int(input())

for i in range(t):
    num, s = input().split()
    text = ""
    for i in s:
        text += int(num)*i
    print(text)
    
    
    





