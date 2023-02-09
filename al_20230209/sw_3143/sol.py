import sys
sys.stdin = open("sample_input.txt")

TC = int(input())

def matching(target,pattern):
    target_l = len(target)
    pattern_l = len(pattern)
    count = 0
    t_idx = 0
    p_idx = 0
    while t_idx < target_l:
        if target[t_idx] == pattern[p_idx]:
            p_idx += 1
            t_idx += 1
        else:                       #여기를 추가했습니다
            t_idx -= p_idx - 1
            p_idx = 0

        if p_idx == pattern_l:
            count += 1
            p_idx = 0
    print(count)

    return count



for T in range(1,TC+1):
    s1 , s2 = input().split()
    # print(matching(s1,s2))
    print(f"#{T}", len(s1) - (matching(s1, s2))*(len(s2)-1))

# T = int(input())
# for tc in range(1, T+1):
#     A, B = input().split()
#     cnt = 0
#     i = 0
#     while i < len(A)-len(B)+1:
#         if A[i:i + len(B)] == B:
#             cnt += 1
#             i += len(B)
#         else:
#             i += 1
#
#     result = (len(A)-(len(B)*cnt)+cnt)
#     print(f'#{tc} {result}')