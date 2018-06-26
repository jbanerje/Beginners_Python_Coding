#Jagannath Banerjee
#Transpose of a matrix
#v1.0 ; Date -7/18/2017


matrix = [[1,2,3]]


row = len(matrix)

column = len(matrix[0])

matrix_T = [list() for f in range(column)]

for i in range(column):
    for j in range(row):
        matrix_T[i].append(matrix[j][i])     

print("Original:", matrix)
print("Transpose:", matrix_T)
