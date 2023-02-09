import sys
sys.stdin = open("test_input.txt",encoding= "UTF-8")

def make_lps(pattern):

    lps = [0] * len(pattern)

    lps_idx = 0
    for i in range(1, len(pattern)):

        if pattern[lps_idx] == pattern[i]:
            lps[i] = lps_idx + 1
            lps_idx += 1
        else:
            lps_idx = 0
            if pattern[i] == pattern[lps_idx]:
                lps[i] = lps_idx + 1
                lps_idx += 1

    return lps

def KMP(pattern, target):
    lps = make_lps(pattern)

    p_idx = 0
    t_idx = 0
    count = 0
    while t_idx < len(target):
        if pattern[p_idx] == target[t_idx]:
            t_idx += 1
            p_idx += 1
        else:
            if p_idx == 0:
                t_idx += 1
            else:
                p_idx = lps[p_idx-1]
        if p_idx == len(pattern):
            count += 1
            p_idx = 0
    return count

for T in range(1,11):
    input()
    pattern = input().strip()
    target = input().strip()
    print(KMP(pattern, target))