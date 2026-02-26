# import numpy
import numpy as np

# define fn
def sum_2_rows( M ) :
    # return 2D array (n/2 , n) -> calculate sum of pair-nearest row
    
    # 1 : slice even row & odd row
    top = M[ 0::2 , : ] # odd row n/2 x n
    bottom = M[ 1::2 , : ] # even row n/2 x n
    
    # 2 : element-wise add matrix
    return top + bottom # n/2 x n

def sum_left_right( M ) :
    # return nxn/2 array -> cut half left-right
    
    # 1 : slice left & right
    left = M[ : , 0 : M.shape[1]//2 : 1 ] # 0:col//2:1
    right = M[ : , M.shape[1]//2 : : 1 ] # col//2::1
    
    # 2 : element-wise add matrix
    return left + right
    
def sum_upper_lower( M ) : # return n/2xn array 
    # 1 : return n/2xn array -> cut half_top * half_bottom
    half_top = M[ 0 : M.shape[0]//2 : 1 , : ] # 0:row//2:1
    half_bottom = M[ M.shape[0]//2 : : 1 ] #row//2::1
    
    # 2 : element-wise add matrix
    return half_top + half_bottom

def sum_4_quadrants( M ) : # return sum of each quadrants
    # 1 : split into 4 subarray (4 quadrants)
    top_left = M[ 0:M.shape[0]//2:1 , 0:M.shape[1]//2:1 ] #htop row , hleft col
    top_right = M[ 0:M.shape[0]//2:1 , M.shape[1]//2::1 ] #htop row , hright col
    bottom_left = M[ M.shape[0]//2::1 , 0:M.shape[1]//2:1 ] #hbottom row , hleft col
    bottom_right = M[ M.shape[0]//2::1 , M.shape[1]//2::1 ] #hbottom row , hright col
    
    # 2 : element-wise add 4 matrices
    return top_left + top_right + bottom_left + bottom_right

def sum_4_cells( M ) : # return sum of each corner
    # 1 : split into 4 subarray (4 corner for each pair)
    top_left = M[ 0::2 , 0::2 ] # odd row , odd col
    top_right = M[ 0::2 , 1::2 ]# odd row , even col
    bottom_left = M[ 1::2 , 0::2 ]# even row , odd col
    bottom_right = M[ 1::2 , 1::2 ]  # even row , even col
    
    # 2 : element-wise add matrix
    return top_left + top_right + bottom_left + bottom_right
    
def count_leap_years( years ) : # years = array 1D
    # return count (int) of leap years
    
    # 1 : make array of bool by checking cd
    ## create 2 cds : %4==0 or (if%100==0 then %400==0)
    years_AD = years - 543 # change to gregorian yr
    
    # cd 1 : divided by 4 (must)
    leap_cd1 = (years_AD % 4 == 0)
    # cd 2 : check years divided by 100 & 400
    leap_cd2_1 = ( (years_AD % 100 == 0) & (years_AD % 400 == 0) )
    leap_cd2_2 = ( (years_AD % 100 != 0) & (years_AD % 400 != 0) )
    
    leap_condition = (leap_cd1) & ((leap_cd2_1) | (leap_cd2_2))
    # 2 : index only True -> index in years
    leap_year = years[ leap_condition ]# index only True cd
    
    # 3 : check length -> years.shape[0] (1D)
    return np.sum(leap_condition) # check length (True = 1)
    # return leap_year.shape[0] can be used

exec(input().strip())