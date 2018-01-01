I = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]

B = [[1,2,3,5], 
     [2,3,3,5], 
     [1,2,5,1]]

def shape(M):
    return len(M),len(M[0])


def matxRound(M, decPts=4):
    rows,cols = shape(M)
    for row in range(rows):
        for col in range(cols):
            M[row][col] = round(M[row][col], decPts)

def transpose(M):
    rows,cols = shape(M)
    table= [ [ 0 for i in range(rows) ] for j in range(cols) ]
    for col in range(cols):
         for row in range(rows):
              table[col][row] = M[row][col]
    return table

print "-------transpose---------"
print shape(I)
print transpose(I)
print shape(B)
print transpose(B)


def matxMultiply(A, B):
    a_rows,a_cols = shape(A)
    b_rows,b_cols = shape(B)
    if a_cols != b_rows:
         raise ValueError

    table = [[0]*b_cols]*a_rows
    t_rows,t_cols =  shape(table)
    res = []
    for t_row in range(t_rows):
        res.append([])
        for t_col in range(t_cols):
            t_sum = 0;
            for num in range(a_cols):
                t_sum = t_sum + A[t_row][num]*B[num][t_col]
            res[t_row].append(t_sum)
    return res

print "------matxMultiply-------"
C = [[1,2],[3,4]]
D = [[5,6,7],[8,9,10]]
print shape(C)
print shape(D)
print matxMultiply(C,D)


def augmentMatrix(A, b):
    a_rows,a_cols = shape(A)
    res = []
    for a_row in range(a_rows):
      res.append([])
      for a_col in range(a_cols):
        res[a_row].append(A[a_row][a_col])
      res[a_row].append(b[a_row][0])
    return res

print "------------augmentMatrix--------------"
E = [[1,2,3],[4,5,6],[7,8,9]]
F = [[1],[2],[3]]
print augmentMatrix(E,F)


def swapRows(M, r1, r2):
    rows,cols = shape(M)
    for col in range(cols):
        temp = M[r2][col]
        M[r2][col] = M[r1][col]
        M[r1][col] = temp

print "--------------swapRows----------------"
swapRows(E, 1, 2)
print E


def scaleRow(M, r, scale):
    if scale != 0:
        rows,cols = shape(M)
        for col in range(cols):
            M[r][col] = M[r][col] * scale
    else:
        raise ValueError

print "--------------scaleRow----------------"
G = [[1,2,3],[4,5,6],[7,8,9]]
scaleRow(G, 1, 2)
print G


def addScaledRow(M, r1, r2, scale):
    if scale != 0:
        rows,cols = shape(M)
        for col in range(cols):
            M[r1][col] =  M[r1][col] + M[r2][col] * scale
    else:
        raise ValueError

print "--------------addScaleRow----------------"
H = [[1,2,3],[4,5,6],[7,8,9]]
addScaledRow(H, 0, 1, 1)
print H


def gj_Solve(A, b, decPts=4, epsilon = 1.0e-16):

    if len(A) != len(b):
        return None

    Ab = augmentMatrix(A,b)
    rows,cols = shape(A)
    
    for col in range(cols):
        maxValue = 0
        maxRowIndex = 0

        for row in range(col,rows):
            if abs(Ab[row][col]) > maxValue:
                maxValue = abs(Ab[row][col])
                maxRowIndex = row
        
        print maxValue,maxRowIndex
        if maxValue < epsilon:
            return None

        print Ab
        swapRows(Ab, col, maxRowIndex)
        print Ab
        scaleRow(Ab, col, 1.0/Ab[col][col])
        print Ab

        for i in range(rows):
            if Ab[i][col] != 0 and i != col:
                addScaledRow(Ab, i, col, -Ab[i][col])
        print Ab

    matxRound(Ab)

    res = []
    for x in range(rows):
        res.append([])
        res[x].append(Ab[x][cols])

    return res

print "--------------gj_Solve----------------"
J = [[7, 5, 3],[-5, -4, 6],[ 2, -2, -9]]
K = [[1],[1],[1]]
print gj_Solve(J, K)

L = [[ -1,  6, -8],[-10, -5,  5],[-9,  2, -4]]
print gj_Solve(L, K)

def calculateMSE(X, Y, m, b):
    n = len(X)
    sum = 0
    for i in range(n):
        sum += (Y[i] - m*X[i] - b)^2
    return sum*1.0/n


def linearRegression(X, Y):
    x_d = []
    for i in range(len(X)):
        x_d.append([])
        x_d[i].append(X[i])
        x_d[i].append(1)

    y_d = []
    for i in range(len(Y)):
        y_d.append([])
        y_d[i].append(Y[i])

    XT = transpose(x_d)
    A = matxMultiply(XT, x_d)
    b = matxMultiply(XT, y_d)
    res = gj_Solve(A, b)
    return res[0][0], res[1][0]



