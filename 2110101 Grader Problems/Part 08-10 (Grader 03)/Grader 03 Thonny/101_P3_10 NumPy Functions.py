# import numpy
import numpy as np

# create fns

# fn1 : checking if same index has more than p%
def eq(A , B , p) :
    # a , b is array (same dimensional)
    # p is percentage (checking if each pos is same)
    # if percent_same > p return True , else return False
    
    # 1 : define bool
    same_pos = (A == B) # array of bool
    
    # 2 : define count_same & count_all
    count_same = np.sum(same_pos) # count only True -> using np.sum
    count_all = np.prod(np.array(A.shape))
    # multiply shape -> change tuple to array -> product
    
    # 3 : define percent_same & check cd. of p
    if (count_same / count_all * 100) >= p : return True
    return False # else not reach p%

# fn2 : add index for colsest point
def closest_point_indexes(points , p) :
    # 1 : broadcast array -> calculate dist
    dxdy_arr = points - p # 2D array (dx , dy)
    
    # 2 : index col for dx , dy array -> element-wise -> got dist_arr
    dx = dxdy_arr[ : , 0] ; dy = dxdy_arr[ : , 1] # 1D array
    dist_arr = ( dx**2 + dy**2 )**0.5 # 1D array
    
    # 3 : create pos. array & min value
    pos_arr = np.arange(dxdy_arr.shape[0]) # range = row of 2D array
    min_dist = np.min(dist_arr) # float
    
    # 4 : check bool
    dist_min_bool = (dist_arr == min_dist) # array of bool
    
    # 5 : return only True pos.
    return pos_arr[ dist_min_bool ]
    
# fn3 : find amount of pair that 
def number_of_inversions(A) : # A is 2D array
    # Logic : make nx1 & 1xn array -> broadcast to nxn array
    # craete array of pos & array of value
    
    # 1 : reshape 1D to 2D array on pos & val array
    pos_row = np.arange(A.shape[0]).reshape( A.shape[0] , 1) # row = i
    pos_col = np.arange(A.shape[0]).reshape( 1 , A.shape[0]) # col = j
    
    val_row = A.reshape( A.shape[0] , 1 ) # row = A[i]
    val_col = A.reshape( 1 , A.shape[0] ) # col = A[j]
    
    # 2 : broadcast -> check cd (got square array)
    inversion = (pos_row < pos_col) & (val_row > val_col) # square array
    return np.sum(inversion) # int (sum only True)

# execute input
exec(input())