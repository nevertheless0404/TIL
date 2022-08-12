import sys

sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-PJT-05/1회차/김유영/_Flatten.txt")

for tc in range(1, 11):
    dump = int(input())
    data = list(map(int, input().split()))

    for i in range(dump):
        # 최댓값의 인덱스를 구해서 할당하고 감소
        max_num = data.index(max(data))
        data[max_num] -=1
        # 최솟값은 증가!
        min_num = data.index(min(data))
        data[min_num] += 1

    # 최솟값과 최대값의 차이를 구하기
    result = max(data) - min(data)

    print('#{} {}'.format(tc, result))