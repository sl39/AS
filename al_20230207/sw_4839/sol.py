import sys
sys.stdin = open("sample_input.txt")

TC = int(input())


def binary_search(start, end, AB):                      # 이진 탐색 리스트 이용
    mid = (start+end)//2
    if mid == AB:
        return 1
    elif mid > AB:
        return binary_search(start, mid, AB)+1
    else:
        return binary_search(mid, end, AB)+1




for T in range(1, TC+1):
    end, Pa, Pb = list(map(int,input().split()))
    start = 1
    A = binary_search(1, end, Pa)
    B = binary_search(1, end, Pb)
    print(f"#{T}", end = " ")
    if A < B:
        print("A")
    elif A > B:
        print("B")
    else:
        print(0)