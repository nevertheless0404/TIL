# 별 찍기
# 홀/ 짝수 번쨰 줄 구분하여 구현
# 짝수번째 경우 공백을 한번 출력

n = int(input())
for star in range(n):
    print("* "*n if star % 2 ==0 else " *"*n)