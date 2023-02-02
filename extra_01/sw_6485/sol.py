import sys
sys.stdin = open("s_input.txt")

TC = int(input())
for test in range(1,TC+1):
    BS  = [0] *(5001)
    N = int(input())
    for i in range(N):
        A,B = map(int,input().split())
        for j in range(A,B+1):
            BS[j] += 1
    P = int(input())
    result = []
    for i in range(P):
        result.append(BS[int(input())])
    print(f'#{test}',*result)
