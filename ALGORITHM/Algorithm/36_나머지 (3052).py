# https://www.acmicpc.net/problem/3052


# 1. 
# 새로운 리스트에 저장 
arr = []
# 10개 수를 입력 
for i in range(10):
    n = int(input())
    # 42로 나누고 객체 추가
    arr.append(n % 42)
# 중복값 제거
arr = set(arr)
print(len(arr))

# 2. 
# for문으로 중복값 제거
arr =[]
for i in range(10):
    n = int(input())
    if n%42 not in arr:
        arr.append(n % 42)

print(len(arr))