import sys
sys.stdin = open("input.txt")

def power(N,M):
    if M == 1:
        return N
    else:
        return N*power(N,M-1)


for T in range(1,11):
    input()
    N, M = map(int,input().split())
    print(f"#{T}",power(N,M))
