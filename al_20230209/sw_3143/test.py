import sys
sys.stdin = open('sample_input.txt')


T = int(input())
for tc in range(1, T + 1):
    A, B = input().split()
    cnt = 0
    i = 0
    while i < (len(A)-len(B)+1):
        for j in range(len(B)):
            if j == len(B) - 1:
                if A[i] == B[j]:
                    cnt += 1
                    i += len(B)
            else:
                if A[i] == B[j]:
                    i += 1
                else:
                    i += 1
                    break



    print(f'#{tc} {len(A)-(cnt)*(len(B)-1)}')