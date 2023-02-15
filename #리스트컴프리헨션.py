#리스트컴프리헨션
m = [ [0 for i in range(5)] for j in [0 for i in range(5)] ] 

row = 0
col = 2

m[row][col] = 1

for i in range(2, 4):
    row -= 1
    col += 1
    if row < 0:
        row = 4
    else:
        m[row][col] = i

m






