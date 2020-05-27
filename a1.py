t = int(input())
for _ in range(t):
    a = []
    for i in range(9):
        a.append(list(input()))
    a[0][0] = a[0][1]
    a[1][3] = a[1][4]
    a[2][6] = a[2][7]
    a[3][1] = a[3][2]
    a[4][4] = a[4][5]
    a[5][7] = a[5][8]
    a[6][2] = a[6][0]
    a[7][5] = a[7][3]
    a[8][8] = a[8][6]
    for i in a:
        print("".join(i))
