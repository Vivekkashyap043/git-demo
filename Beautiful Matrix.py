
matrix = []
tempi = 0
tempj = 0
for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)
for i in range(5) :
    for j in range(5) :
        if matrix[i][j] != 0:
            tempi = i
            tempj = j
            break
print(abs(2-tempi)+abs(2-tempj))    
    
