# https://www.acmicpc.net/problem/1157

# 대소문자를 구분하지 않는다.
words = input().upper()
# set으로 형 변환을 시켜 중복 제거  
Alp = list(set(words))
# 반복문을 돌려 i값이 몇 번 쓰였는지 확인
count_list =[]
for i in Alp:
    count = words.count(i)
    count_list.append(count)
# print(count_list)
# 2개 이상 사용된 것은 ? 
if count_list.count(max(count_list)) >= 2:
    print('?')
    # count_list중에 count가 가장 많이 선언된 index의 위치를 반환하고 그 값은 넣어준다.
else:
    print(Alp[count_list.index(max(count_list))])
