#Matrix addition function
def perform_matrix_addition(matrix_A,matrix_B):
    matrix_row = 0
    matrix_row_element = 0
    matrix_added_row=[]
    matrix_addition = []

    for matrix_row in range(len(matrix_A)):
        for matrix_row_element in range(len(matrix_A[matrix_row])):
            #print("Elements ",matrix_row, matrix_row_element,":",matrix_A[matrix_row][matrix_row_element])
            matrix_added_row.append( matrix_A[matrix_row][matrix_row_element] + matrix_B[matrix_row][matrix_row_element])
        matrix_addition.append(matrix_added_row)
        matrix_added_row=[]

    #print ("matrix_addition:", matrix_addition)
    return matrix_addition

#Matrix subtraction function
def perform_matrix_subtraction(matrix_A,matrix_B):
    matrix_row = 0
    matrix_row_element = 0
    matrix_sub_row = []
    matrix_subtraction = []

    for matrix_row in range(len(matrix_A)):
        for matrix_row_element in range(len(matrix_A[matrix_row])):
            #print("Elements ",matrix_row, matrix_row_element,":",matrix_A[matrix_row][matrix_row_element])
            matrix_sub_row.append( matrix_A[matrix_row][matrix_row_element] - matrix_B[matrix_row][matrix_row_element])
        matrix_subtraction.append(matrix_sub_row)
        matrix_sub_row = []
        
    #print ("matrix_subtraction:", matrix_subtraction)
    return matrix_subtraction

#Matrix Multiplication
def perform_matrix_multiplication(matrix_A,matrix_B,matrix_row_A,matrix_row_B,matrix_col_A,matrix_col_B):   
    matrix_row = 0
    matrix_col = 0
    matrix_row_element = 0
    matrix_col_element = 0
    matrix_mul_row = []
    matrix_multiplication = [1,1,1,1,1]

    print(matrix_row_A,"X",matrix_col_B)
    
    for matrix_row_A in range(matrix_row_A):
        for matrix_row_element_A in range(len(matrix_A[matrix_row_A])):
            print("Matrix-A[",matrix_row_A,",",matrix_row_element_A,"]=",matrix_A[matrix_row_A][matrix_row_element_A])

    print("--------------------------------")
    
    for matrix_row_B in range(len(matrix_B)):

        col_b_int = 0
        while col_b_int < matrix_col_B:
            for matrix_col_element_B in range(len(matrix_B[matrix_row_B])):
                print("Matrix-B[",matrix_row_B,",",col_b_int,"]=",matrix_B[col_b_int][matrix_col_element_B]) 
                col_b_int = col_b_int + 1
                
    return matrix_multiplication

    

#Creating the matrix
def create_matrix(matrix_row , matrix_col ):

    row = 1
    matrix=[]
    row_element_int = []

    while (row <= matrix_row) :
        print("Row : ",row)
        row_element_raw = input("Enter the elements with ',':")
        row_element = row_element_raw.split(",")

        for element_str in row_element:
            row_element_int.append(int(element_str ))

        matrix.append(row_element_int)
        row_element_raw = ""
        row_element_int = []
        row = row + 1

    return matrix

#Main Function - The actual Driver Para
def main():
    count = 0
    
    matrix_col_A = ""
    matrix_row_A = ""
    matrix_add_res = []
    matrix_sub_res = []
    matrix_mul_res = []
    
    #Build Matrix A
    matrix_row_A, matrix_col_A = input("Enter 'Row , Column' of Matrix A :").split(',')
    matrix_row_A = int(matrix_row_A)
    matrix_col_A = int(matrix_col_A)

    matrix_A = create_matrix(matrix_row_A , matrix_col_A )    
    print("Matrix A (", matrix_row_A ,"X", matrix_col_A,")=",matrix_A)

    #Build Matrix B
    matrix_row_B, matrix_col_B = input("Enter 'Row , Column' of Matrix B :").split(',')
    matrix_row_B = int(matrix_row_B)
    matrix_col_B = int(matrix_col_B)

    matrix_B = create_matrix(matrix_row_B , matrix_col_B )    
    print("Matrix B (", matrix_row_B ,"X", matrix_col_B,")=",matrix_B)

    #Perform Matrix Addition / Subtraction / Multiplication

    if ( (matrix_row_A == matrix_row_B) & (matrix_col_A == matrix_col_B) ):

        matrix_add_res = perform_matrix_addition(matrix_A,matrix_B)
        print("Matrix_addition:", matrix_add_res)

        matrix_sub_res = perform_matrix_subtraction(matrix_A,matrix_B)
        print("Matrix_subtraction:", matrix_sub_res)

        matrix_mul_res = perform_matrix_multiplication(matrix_A,matrix_B,matrix_row_A,matrix_row_B,matrix_col_A,matrix_col_B)
        print("Matrix_multiplication:", matrix_mul_res)
                
    else:
        print("Matrix Additional/Subtraction must have same rows & columns")

        if (matrix_col_A == matrix_row_B):
            print("Resultant Matrix-",matrix_row_A , matrix_col_B )
            matrix_mul_res = perform_matrix_multiplication(matrix_A,matrix_B,matrix_row_A,matrix_row_B,matrix_col_A,matrix_col_B)
            print("Matrix_multiplication:", matrix_mul_res)
        

#Main Clause
if __name__ == "__main__":
    main()
