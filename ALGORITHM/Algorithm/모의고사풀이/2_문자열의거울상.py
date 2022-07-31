import sys

sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-PJT-03/1회차/김유영/_문자열의거울상.txt")
T = int(input())
# ex) 'bdppq' => 'pqqbd'
# 문자열을 뒤집어서 풀기 
for test_case in range(1, T+1):
    case = input()
    text = ''
    for i in case[::-1]:
        if i == 'b':
            text += 'd'
        elif i == 'd':
            text += 'b'
        elif i == 'p':
            text += 'q'
        else:
            text += 'p'
    print('#{}'.format(test_case),text)
