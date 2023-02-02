import sys
sys.stdin = open("s_input.txt")

T = int(input())
for test in range(1,T+1):
    D,A,B,F = map(int,input().split())
    print(f"#{test}",D*F/(A+B))