#Soumik Bhattacharyya, Roll-1811155
'''
A3/Q1. Write a Gauss-Jordan code with partial pivoting and solve the following set of linear equations.
x +3y +2z =2
2x +7y +7z =-1
2x +5y +2z =7
'''
#The matrix formed by the numerical coefficient is written in a separate txt file and read from there.

#reading the matrix
with open("m1.txt", 'r') as a:
    matrix = [[int(num) for num in row.split(' ')] for row in a]

vector= [2, -1, 7] #vector formed by the right hand side of equations

n=3 #number of equations

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
        for j in range (i,n):
            m[i][j] = m[i][j]/factor1
        v[i] = v[i]/factor1

        for k in range (n):
            if k!=i and m[k][i]!=0:
                factor2 = m[k][i]
                for l in range (i,n):
                    m[k][l] = m[k][l] - factor2*m[i][l]
                v[k] = v[k] - factor2* v[i]

gauss_jordan (matrix, vector)

print("The soltion set of the linear equations is:")
print("x=", vector[0])
print("y=", vector[1])
print("z=", vector[2])


'''
The soltion set of the linear equations is:
x= 3.0
y= 1.0
z= -2.0
'''

