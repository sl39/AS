# # import sys
# from itertools import permutations
# # sys.stdin = open("sample_input.txt")
#
# TC = int(input())
# for T in range(1,TC+1):
#     mat = []
#     n = int(input())
#     for i in range(n):
#         mat.append(list(map(int,input().split())))
#     mat = [0]* (10**100)

import sys
import psutil
from itertools import permutations
sys.stdin = open("sample_input.txt")

def check_memory(tc):
    ps = psutil.Process()
    rss = ps.memory_info().rss / 2**20 # byte to MB
    print(f'{tc} : {rss}')

TC = int(input())
for T in range(1,TC+1):
    mat = []
    n = int(input())
    for i in range(n):
        mat.append(list(map(int,input().split())))
    ls = list(range(n))
    ls = list(permutations(ls,n))
    mx = n* 10
    for i in ls:
        mys = 0
        for j in range(n):
                mys += mat[j][i[j]]
        mx = min(mx,mys)
    print(check_memory(T))
    print(f"#{T}",mx)