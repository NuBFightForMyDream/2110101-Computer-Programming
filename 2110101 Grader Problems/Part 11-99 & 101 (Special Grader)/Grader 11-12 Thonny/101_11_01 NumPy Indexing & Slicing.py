# Note : NumPy Array Commands
# a.shape = (1D , 2D , 3D) (1D = row , 2D = (row,col) , 3D = (row,col,len))
# beware of 1D and 2D array

# a[ choose_row , choose_col ] (choose_row , choose_col is slicing)

## --> Can choose array by list of index too
# Ex : a[ [list of id] ]
# choose (id1 , ids) as row,col : a[ [list of id1] , [list of id2] ]
# a = [ arr[id11] , arr[id22] , arr[id33] ]

# 1 : create fns
import numpy as np

# A is 2D array (row x col) -> A = np.array(list of list) = array 2D

def get_column_from_bottom_to_top(A , c) :
    # get column #c reversed
    choosecol_reverse = A[ ::-1 , c]  # choose all row reverse  , choose col #c
    # return array
    return choosecol_reverse # array() -> print will return in array form

def get_odd_rows( A ) :
    # get odd row (start row #1 step 2) , all column
    oddrow_allcol = A[ 1::2 , :: ]
    # return array
    return oddrow_allcol # array() -> print will return in array form

def get_even_column_last_row( A ) :
    # get even row (start row #0 step 2) , last column (column # -1)
    lastrow_evencol = A[ -1 , 0::2 ]
    # return array
    return lastrow_evencol # array

def get_diagonal1( A ) : # A = square matrix
    # diagonal (\) left_top corner to right_bottom corner
    # pattern : [0,0] , [1,1] , [2,2] , ... , [n,n] ==> define row & col range
    
    # define row & col list
    row = list(range(0 , A.shape[0] , 1)) # list (create list with range)
    col = list(range(0 , A.shape[1] , 1)) # list (create list with range)
    # btw -> make array 1D (list) can be done too : np.arange(...) in row,col
    
    # slice each element in array
    diagonal1 = A[ row , col ] # pick pair of elements in row & col -> r0c0 , r1c1 , ...
    return diagonal1 # array

    ## or can use A.diag()
    
def get_diagonal2( A ) :
    # diagonal (/) right_top corner to left_bottom corner
    # pattern [0,n] , [1,n-1] ,... ,[n,0]
    
    # define row & col list
    row = list(range(0 , A.shape[0] , 1))
    col_reverse = list(range(-1 , -A.shape[1]-1 , -1)) # add -1 at stop cuz we need col 0 too

    # slice each element in array
    diagonal2 = A[row , col_reverse]
    return diagonal2 # array

exec(input().strip())