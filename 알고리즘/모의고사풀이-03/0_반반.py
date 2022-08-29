import sys
from tabnanny import check

sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-PJT-05/1회차/김유영/_반반.txt")


T = int(input())
 
for tc in range(1, 1 + T):
    # 문자를 리스트로 받는 s
    s = list(input())

    check = True
 
    # 반복문 돌면서 값이 2면 끝 
    # 그 외에는 check를 True로 바꿔준다. 
    for i in s:
        if s.count(i) == 2:
            continue
 
        else:
            check = False
            break
 
    if check == False:
        print('#{} {}'.format(tc, 'No'))
 
    else:
        print('#{} {}'.format(tc, 'Yes'))

    


       