# 월이 입력될 때 계절 이름이 출력되도록 해보자.

month = int(input())

if month//3==1:
    print("spring")
elif (month-3)//3==1:
    print("summer")
elif (month-6)//3==1:
    print("fall")
else:
    print("winter")