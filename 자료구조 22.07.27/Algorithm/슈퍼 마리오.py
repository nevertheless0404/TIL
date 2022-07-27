# https://www.acmicpc.net/problem/2851


m = []
score = 0
for i in range(10):
    # 숫자를 정렬해서 정리한다.
    m.append(int(input()))
for j in m:
     # 숫자들을 차례대로 더해간다.
    score += j
    # print(score)
    # 100보다 작은 같은 양의 정수
    if score >= 100:
        # 숫자를 더했을 때, 숫자와 더하지 않았을 때는 비교 하여 100과 가까운 
        # 수를 구하고 버섯 먹은 것을 중단하면 멈춤!
        if score - 100 > 100 - (score - j):
            score -= j
            break
print(score)