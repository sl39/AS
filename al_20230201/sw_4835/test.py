# import sys
# sys.stdin = open('sample_input.txt')

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    sum_list = []
    for j in range(N-M+1):
        sum_num = 0
        for k in arr[j:j+M]:
            sum_num += k
        sum_list.append(sum_num)
    max_nums = sum_list[0]
    min_nums = sum_list[0]
    for x in range(1, N-M+1):
        if max_nums < sum_list[x]:
            max_nums = sum_list[x]
        if min_nums > sum_list[x]:
            min_nums = sum_list[x]
    result = max_nums - min_nums
    print(f'#{i+1} {result}')