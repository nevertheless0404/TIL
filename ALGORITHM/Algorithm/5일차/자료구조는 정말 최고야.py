# https://www.acmicpc.net/problem/23253

import sys
input = sys.stdin.readline

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220801/자료구조는 정말 최고야.txt")

n, m = map(int, input().split())

# 정렬이 가능 여부
possible = True
for i in range(m):
    # 책 리스트
    book_list = int(input())
    # 책 더미
    book_heap = list(map(int, input().split()))
    # 책 더미의 정렬 여부 확인
    # 내림차순이 아니라면 올바르게 정렬할수없다.
    for j in range(book_list-1):
        if book_heap[j] < book_heap[j+1]:
            possible = False
           
if possible:
    print('Yes')
else:
    print('No')
    
    