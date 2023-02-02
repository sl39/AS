import sys
# open 함수의 인자로 들어가는
# 문자열은 내가 열고자 하는 파일의 "경로"와 이름입니다.
sys.stdin = open('./input.txt')
TC =int(input())
for i in range(TC):
    N = int(input())
    ls = list(map(int , input().split()))
    result = 0
    for j in range(N):
        my = 0
        for k in range(j+1,N):
            if ls[j] > ls[k]:
                my += 1
        if result < my:
            result = my
    print(f"#{i+1}",result)



# map 의 첫번쨰 인자는 함수
# 두번째 인자는 순회 가능한 요소
# 순회 가능한 요소가 가진 각 값들을
# 첫번쨰 인자에 작성한 함수에 대입하여 실행
# 실행한 결과를 모아서 map Object로 반환