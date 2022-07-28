# https://www.acmicpc.net/problem/7785

n = int(input())
log = {}
for i in range(n):
    name, state = input().split()
    if state == 'enter':
        # 출근을 value에서 1
        log[name] = 1
    else: 
        log[name] = 0

names = []
# 반복문을 돌리면서 아직 퇴근하지 않은 직원의 이름을 저장
for name in log:
    if log[name] == 1:
        names.append(name)
for name in names:
    print(name)