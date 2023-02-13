import sys
sys.stdin = open('sample_input.txt')

TC = int(input())
for T in range(1,TC+1):
    stack = []
    ls = input().strip()
    top = -1
    for i in range(len(ls)):
        if top > -1 and stack[top] == ls[i]:
            stack.pop()
            top -= 1
        else:
            stack.append(ls[i])
            top += 1
    print(f"#{T}",top + 1)