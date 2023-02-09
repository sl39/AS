import sys
sys.stdin = open("input.txt")
for T in range(1,11):
    mat =[]
    input()
    for i in range(100):
        mat.append(list(map(int,input().split())))
    start = []
    for i in range(100):
        if mat[0][i] == 1:
            start.append(i)
    res1 = 10000
    res2 = 0

    for i in start:
        x = 0
        y = i
        count = 0

        while x < 99:
            while x+1< 100 and mat[x+1][y]:
                x = x+1
                count += 1
                if y+1 < 100 and mat[x][y+1]:
                    break
                if 0<= y-1 and mat[x][y-1]:
                    break

            while y+1 < 100 and mat[x][y+1]:
                y = y+1
                count += 1
                if x+1< 100 and mat[x+1][y]:
                    x = x+1
                    count += 1
                    break

            while 0<= y-1  and mat[x][y-1]:
                y = y-1
                count += 1
                if x+1< 100 and mat[x+1][y]:
                    x = x+1
                    count += 1
                    break
        
        if count <= res1:
            res1 = count
            res2 = i






    print(f"#{T}",res2,start)
        
