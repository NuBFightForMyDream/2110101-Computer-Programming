# import numpy first
import numpy as np

# 1 : define fn
def mult_table(nrows , ncols) :
    # define ndarray first -> int array
    # cmd : np.ndarray( shape , type ) # shape = tuple
    mult_arr = np.ndarray((nrows , ncols) , int) # shape = (row , col)
    
    # define 1D array first -> reshape to 2D array
    # step : arange for 1D array -> reshape
    arr_row = np.arange(1 , nrows+1).reshape(nrows , 1) # 1 col (2D)
    arr_col = np.arange(1 , ncols+1).reshape(1 , ncols) # 1 row (2D)
    
    # choose all -> multiply (element-wise op.)
    mult_arr[:,:] = arr_row * arr_col
    
    # return array nxn
    return mult_arr

# execute fn
exec(input().strip())