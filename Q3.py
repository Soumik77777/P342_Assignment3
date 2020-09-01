#Soumik Bhattacharyya, Roll-1811155
'''
A3/Q3. Find the inverse of the matrix (inverse exists) and check if AA-1=I.
     1 -3  7
A=  -1  4 -7
    -1  3 -6
'''

#reading the matrix
with open("m3.txt", 'r') as a:
    matrix = [[int(num) for num in row.split(' ')] for row in a]

matrix_id = [[1,0,0],[0,1,0],[0,0,1]]

n= len(matrix)

#Function for Partial pivoting
def pp (m, v):
    for i in range (n-1):
        if m[i][i] ==0:
            for j in range (i+1,n):
                if abs(m[j][i]) > abs(m[i][i]):
                    m[i], m[j] = m[j], m[i]
                    v[i], v[j] = v[j], v[i]

#Function for Gauss-Jordan
def gauss_jordan (m, v):
    pp(m, v)
    for i in range (n):
        factor1 = m[i][i]
        for j in range (n):
            m[i][j] = m[i][j]/factor1
        for q in range (n):
            v[i][q] = v[i][q]/factor1

        for k in range (n):
            if k!=i and m[k][i]!=0:
                factor2 = m[k][i]
                for l in range (i,n):
                    m[k][l] = m[k][l] - factor2*m[i][l]
                for r in range (n):
                    v[k][r] = v[k][r] - factor2* v[i][r]

#Inverse part
gauss_jordan (matrix, matrix_id)

print("The inverse of the given matrix is:")
for i in range(n):
    print(matrix_id[i])
print("This matrix should give the identity matrix when multiplied with the original matrix.")

#Function for matrix-multiplication
def matrix_multi (matrix_m, matrix_n):
    matrix_L = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                matrix_L[i][j] += matrix_n[k][j] * matrix_m[i][k]
    return matrix_L

#Verification part
with open("m3.txt", 'r') as a:
    matrixA = [[int(num) for num in row.split(' ')] for row in a]

x = matrix_multi (matrixA, matrix_id)

print("The result of A*A-1 is:")
for i in range(n):
    print(x[i])

if x==[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]:
    print("This is the identity matrix, i.e. the inverse was correct.")
else:
    print("The inverse of the matrix is incorrect")

'''
The inverse of the given matrix is:
[-3.0, 3.0, -7.0]
[1.0, 1.0, 0.0]
[1.0, 0.0, 1.0]
This matrix should give the identity matrix when multiplied with the original matrix.
The result of A*A-1 is:
[1.0, 0.0, 0.0]
[0.0, 1.0, 0.0]
[0.0, 0.0, 1.0]
This is the identity matrix, i.e. the inverse was correct.

'''

