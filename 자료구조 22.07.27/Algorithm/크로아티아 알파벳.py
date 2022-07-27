# https://www.acmicpc.net/problem/2941


A = ('c=','c-','dz=','d-','lj','nj','s=','z=')
B = input()
for i in A:
    # 문자열에서 값을 찾아준다. 
    B = B.replace(i, 'A')
# 길이를 출력한다.
print(len(B))