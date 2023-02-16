import sys
sys.stdin = open("sample_input.txt")


def result(start,end):
    if rsp[start] == rsp[end]:
        return start
    elif rsp[start] == 1:
        if rsp[end] == 2:
            return end
        else:
            return start
    elif rsp[start] == 2:
        if rsp[end] == 3:
            return end
        else:
            return start
    else:
        if rsp[end] == 1:
            return end
        else:
            return start


def r(start,end):
    if start == end:
        return start
    elif end - start == 1:
        return result(start,end)
    else:
        return result(r(start,(start+end)//2),r((start+end)//2+1,end))


TC = int(input())
for T in range(1,TC+1):
    N = int(input())
    rsp = list(map(int,input().split()))
    print(f"#{T}", r(0,N-1)+1)

