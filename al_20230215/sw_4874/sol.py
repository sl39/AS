import sys
sys.stdin = open("sample_input.txt")

TC = int(input())
for T in range(1,TC+1):
    fourth = list(map(str,input().split()))
    stack = []
    cnt = 1
    for i in fourth:
        if i == ".":
            pass
        elif i in "+*/-":
            try:
                A = stack.pop()
                B = stack.pop()
            except:
                cnt = 0
                break
            if i == "+":
                C = B + A
            elif i == "*":
                C = B * A
            elif i == "-":
                C = B - A
            else:
                C = int(B/A)
            stack.append(C)
        else:
            stack.append(int(i))
    print(f"#{T}", end = " ")
    if cnt:
        if len(stack) == 1:
            print(stack[0])
        else:
            print("error")
    else:
        print("error")

