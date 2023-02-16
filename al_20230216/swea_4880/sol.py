import sys
sys.stdin = open("sample_input.txt")

ls = [0,3,1,2]
def result(start,end):                          ## 두 점의 가위바위보를 구하는 함수
    if ls[rsp[end]] == rsp[start]:
        return end
    else:
        return start


def r(start,end):
    if start == end:                ## 만약에 시작과 끝이 같다면 
        return start                ## start 를 리턴
    else:
        return result(r(start,(start+end)//2),r((start+end)//2+1,end))  ## 아니라면 다른 두 그룹에서 이기고 올라온 애들을 싸움시킨애를 리턴



TC = int(input())
for T in range(1,TC+1):
    N = int(input())
    rsp = list(map(int,input().split()))
    print(f"#{T}", r(0,N-1)+1)

