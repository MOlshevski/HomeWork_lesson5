from random import randint

matrix = []
rows = columns = 3  # The number of rows and columns of the matrix

for i in range(rows):  # The cycle to fill the matrix with random digits
    matrix.append([])
    for j in range(columns):
        matrix[i].append(randint(1, 9))

for row in matrix:  # The cycle to output the matrix in the usual form
    print(row)

#  Condition for determining matrix symmetry
if matrix[0][1] == matrix[1][0] and matrix[0][2] == matrix[2][0] and matrix[1][2] == matrix[2][1]:
    print('This matrix is symmetric')
else:
    print('This matrix is not symmetric')
