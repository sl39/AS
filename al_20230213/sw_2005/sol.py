import sys
sys.stdin = open("input.txt")

TC = int(input())

def fact(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return fact(n-1) * n

def combination(n,r):
    if r == 0:
        return 1
    else:
        return int(fact(n)/(fact(r)*fact(n-r)))


for T in range(1,TC+1):
    N = int(input())
    print(f"#{T}")
    for i in range(0,N):
        for j in range(i+1):
            print(combination(i,j),end=" ")
        print()


