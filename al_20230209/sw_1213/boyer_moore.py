import sys
sys.stdin = open("test_input.txt",encoding= "utf-8")


def search(pattern, char):
    for i in range(len(pattern)-2,-1,-1):
        if pattern[i] == char:
            return len(pattern) - i -1
    return len(pattern)
def boyer_moore(pattern, target):
    count = 0
    t_idx = 0

    while t_idx <= len(target) - len(pattern):
        p_idx = len(pattern) - 1

        while p_idx >= 0:
            if pattern[p_idx] != target[t_idx + p_idx]:
                next = search(pattern, target[t_idx+len(pattern) - 1])
                break
            p_idx -= 1
        if p_idx == -1:
            count += 1
            t_idx += 1
        else:
            t_idx += next
    return count







for _ in range(10):
    tc = int(input())
    pattern = input()
    target = input()
    print(boyer_moore(pattern,target))