# https://www.acmicpc.net/problem/1292




# A, B를  입력 받고 0에서 B까지 반복
A, B = map(int, input().split())
arr = []
for i in range(1, B+1):
    # i 만큼 반복해서 리스트 arr에 넣어줌
    for j in range(i):
        arr.append(i)
print(sum(arr[A-1:B]))


# 2.
# arr = []
# numbers = 1
# while len(arr) < B:
# # number의 크기만큼 수열 리스트에 n을 추가한다.
#     for i in range(numbers):
#         arr.append(numbers)
#         numbers += 1
# print(arr,len(arr))