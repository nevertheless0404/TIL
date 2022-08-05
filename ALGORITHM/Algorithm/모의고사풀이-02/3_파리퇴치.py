import sys

sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-PJT-04/1회차/김유영/_파리퇴치.txt")

t = int(input())
for tc in range(1, t+1):
    # 행열 수 n, 파리채 크기 M
    n,m = map(int, input().split())
    # N*N 배열 입력 받기
    line = [list(map(int, input().split()))for _ in range(n)]

    # 죽은 파리 수 저장
    die = 0
    # M의 크기가 1일 경우 , 모든 배열 공간을 파리채로 휘두를 수 있지만, 
    # 파리채가 커지게 되면 탐색할 공간이 줄어들기 때문에 범위를 조절
    for i in range(n-m+1):
        for j in range(n-m+1):
            # 파리의 갯수를 초기화 
            fly = 0
            # 파리채로 타격했을 때 죽일 수 있는 파리의 수 탐색 
            for k in range(m):
                for l in range(m):
                    fly += line[i+k][j+l]
            if fly > die:
                die = fly
    print('#%d %d' % (tc, die))
        

    
            
        




    