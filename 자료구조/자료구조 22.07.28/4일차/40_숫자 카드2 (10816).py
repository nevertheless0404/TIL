# https://www.acmicpc.net/problem/10816

# 숫자카드의 개수
N = int(input())
# 숫자카드의 정수 
arr_n = list(map(int, input().split()))
# 정수 
M = int(input())
# 상근이가 가지고 있는 카드 수 
arr_m = list(map(int, input().split()))

dict1 = dict()
# 숫자카드와 개수를 딕셔너리에 담기
for i in arr_n:
    if i in dict1:
        dict1[i] += 1
    else: 
        dict1[i] = 1

for i in arr_m:
    if i in dict1:
        print(dict1[i], end=" ")
    else:
        print(0, end=" ")