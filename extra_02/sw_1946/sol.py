import sys
sys.stdin = open("input.txt")

TC = int(input())
for T in range(1,TC+1):
    Cis = []
    Kis = []
    N = int(input())
    result = ""
    for i in range(N):
        Ci, Ki = map(str,input().split())
        result += Ci * int(Ki)
    rl = len(result)//10
    print(f"#{T}")
    for i in range(rl):
        print(result[i*10:(i+1)*10])
    print(result[rl*10:])