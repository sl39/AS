import sys

sys.stdin = open('input.txt')

for tc in range(6):
    number = int(input())

    num = []
    if number > 0:
        while number:
            num.append(number % 10 + 48)

            number = number // 10
        num = num[::-1] # 1+48 6+48 4+48 1+48 -> 49 52 54 49
    else:
        number = abs(number)
        while number:
            num.append(number % 10 + 48)

            number = number // 10
        num.append(45) # 음수이기 때문에 45를 맨 뒤에 추가하면 된다.
        num = num[::-1] # 그럼 다시 맨앞에 -나옴
    # str로 바꿔준다.
    st = ""
    for i in num:
        st += chr(i)
    print(f'#{tc+1}', st, type(st))