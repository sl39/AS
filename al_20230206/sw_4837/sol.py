### 아이디어
## 첫번째로 칸과 칸 사이의 모든 칸을 각각의 리스트에 저장


import sys
sys.stdin = open("sample_input.txt")

TC = int(input())
for T in range(1,TC+1):
    red = []                # 빨간색 칸을 넣을 리스트 생성
    blue = []               # 파란색 칸을 넣을 리스트 생성
    s = int(input())
    for line in range(s):
        x1, y1, x2, y2, color = map(int,input().split())
        if color == 1:                      # color 가 1이면  red에넣음
            for i in range(x1,x2+1):        # 두 좌표의 사이의 모든 칸을 red에넣음
                for j in range(y1,y2+1):
                    red.append((i,j))
        else:                           # color 가 2이면  blue 에넣음
            for i in range(x1,x2+1):    # 두 좌표의 사이의 모든 칸을 blue 에넣음
                for j in range(y1,y2+1):
                    blue.append((i,j))
    red = set(red)                  # red에 있을 중복값 제거
    blue = set(blue)                # blue에 있을 중복값 제거
    print(f"#{T}",len(red & blue))  # 그리고 두 집합의 교집합 생성