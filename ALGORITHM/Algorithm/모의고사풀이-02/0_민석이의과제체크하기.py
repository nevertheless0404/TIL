import sys

sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-PJT-04/1회차/김유영/_민석이의과제체크하기.txt")

t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    submit = list(map(int, input().split()))
    no_submit =[]

    # 반복문의 범위로 설정
    # 제출하지 않았다면 결과값에 넣어주기
    for i in range(1, n+1):
        if i not in submit:
            no_submit.append(i)

    print('#{}'.format(tc),end = " ")
    for i in no_submit:
        print(i, end=" ")
    print()




