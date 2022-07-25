# X보다 작은 수 
# 정수 N로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력


# 반복문으로 한 값씩 가져오기!
n, x = map(int, input().split())
a = list(map(int, input().split()))

for i in a:
    if i < x:
        print(i , end=" ")