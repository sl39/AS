import sys
sys.stdin = open("input.txt")

TC = int(input())
prime_list = [2,3,5,7,11]
for T in range(1,TC+1):
    ls = [0] *5
    N = int(input())
    for i in range(5):
        while True:
            if N%prime_list[i] == 0:
                ls[i] += 1
                N = N//prime_list[i]
            else:
                break
    print(f"#{T}",*ls)