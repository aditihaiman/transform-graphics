"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    for x in range(4):
        line = ""
        for y in range(len(matrix)):
            if(matrix[y][x]//10 == 0): line += str(matrix[y][x]) + "   "
            elif(matrix[y][x]//10 < 10): line += str(matrix[y][x]) + "  "
            else: line += str(matrix[y][x]) + " "
        print(line)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            matrix[x][y] = 0
            if(x == y): matrix[x][y] = 1
            

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    m21 = []
    copy(m2, m21)
    for x in range(len(m2[0])):
        for y in range(len(m1)): #for each col in m1
            sum = 0
            for z in range(len(m2)):
                sum += m1[z][x] * m21[y][z]
                #print(sum)
            m2[y][x] = sum

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

def copy(m1, m2):
    for list in m1:
        l = []
        for x in list:
            l.append(x)
        m2.append(l)
