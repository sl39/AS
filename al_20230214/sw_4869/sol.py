import sys
sys.stdin = open("sample_input.txt")

def fact(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return fact(n-1) * n


def com(n,r):
    if r == 0:
        return 1
    else:
        return fact(n)/(fact(r)*fact(n-r))

TC = int(input())
for T in range(TC):
    N = int(input())
    N = N//10
    if N % 2 == 0:
        A = N//2
        result = 0
        r = 0
        while A >= 0:
            result += (2**A)*(com(A+r,r))
            A -= 1
            r += 2
    else:
        A = N//2
        result = 0
        r = 1
        while A >= 0:
            result += (2**A)*com(A+r,r)
            A -= 1
            r += 2
    print(int(result))
