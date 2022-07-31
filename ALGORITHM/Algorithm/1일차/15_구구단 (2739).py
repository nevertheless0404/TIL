# 구구단
# n을 입력받은 뒤, 구구단 n단을 출력하는 프로그램


numbers = int(input())
for goo in range(1, 10):
    print(numbers,"*",goo, "=", numbers*goo)