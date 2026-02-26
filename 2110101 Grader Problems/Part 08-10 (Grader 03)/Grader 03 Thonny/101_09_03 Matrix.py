# define 3 fns

# 1 : read matrix -> input , return list of list
def read_matrix() :
    # 1.1 : define empty matrix (list of list)
    matrix = []
    nrows = int(input()) # row = outer index
    for k in range(nrows) :
        # 1.2 : enter element in matrix
        r = [] # empty sublist (1-row matrix)
        x = input().split() # x = each element in 1 row
        for e in x :
            r.append(float(e))
        # out of loop -> append sublist
        matrix.append(r)
    # out of loop -> return matrix
    return matrix

# 2 : multiply with const.
def mult_c(c , A) :
    # 2.1 : call read_matrix first
    # A = read_matrix() # return result in matrix
    # 2.2 : for loop each element
    for i in range(len(A)) :
        for j in range(len(A[i])) :
            A[i][j] = c * A[i][j]
    # out of loop -> return matrix
    return A
        
def mult(A , B) :
    # define empty list
    C = []
    # define nested loop (orw & col)
    for rowA in range(len(A)) : # rowA
        sub_C = [] # define sublist for appending val.
        for colB in range(len(B[0])) : # colB
            sum_c = 0
    ## See logic of (3,2)X(2,3) = (3,3)     
    # Ex : [[00,01],[10,11],[20,21]] x [[00,01,02],[10,11,12]]
    # write in paper will see pattern
            for colA in range(len(A[0])) : # colA -> range of dot-product
                sum_c += A[rowA][colA] * B[colA][colB] # colA = rowB
            # append c to sub_C
            sub_C.append(sum_c)
        # append to big list
        C.append(sub_C)
    # return C
    return C
exec(input().strip())   