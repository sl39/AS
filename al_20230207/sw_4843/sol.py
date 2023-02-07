import sys
sys.stdin = open("sample_input.txt")

TC = int(input())


for T in range(1,TC+1):
    N = int(input())
    ls = list(map(int,input().split()))
    ls = sorted(ls)                             # 리스트를 정렬해주고

    new_ls = []

    for i in range(10):
        if i%2 == 0:                            #i가 짝수면 큰거를 추가
            new_ls.append(ls[-1-(i//2)])
        else:
            new_ls.append(ls[i//2])             #i가 홀수면 작은것을 추가
    print(f"#{T}",*new_ls)