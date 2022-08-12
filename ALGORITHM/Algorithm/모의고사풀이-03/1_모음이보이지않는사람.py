import sys

sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-PJT-05/1회차/김유영/_모음이보이지않는사람.txt")

t = int(input())
for tc in range(1, t+1):
    words = input()
    # 모음 제거 후 문장(단어)
    answer = ''

    for i in words:
        # 모음이 아니면 넣어주기!
        if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u':
            answer += i

    print('#{} {}'.format(tc, answer))
