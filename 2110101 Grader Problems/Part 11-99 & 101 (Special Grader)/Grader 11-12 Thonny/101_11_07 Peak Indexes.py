# import numy first
import numpy as np

# define fns
def peak_indexes(x) : # return array of pos. in peaks
    # x = 1D array -> return array of peaks
    
    # 1 : check peaks condition (consider only 1 to -1)
    # using element-bool operation -> check arr
    # Ex : [1,2,3,4] => [1,2] check [2,3] check [3,4]
    
    # 1.1 : slice left , mid , right array
    left = x[0:-2] # check 0 to 3rd last
    mid = x[1:-1] # check 1 to 2nd last
    right = x[2:] # check 2 to last
    
    # 1.2 -> do element-wise bool op.
    peaks_strip = (left < mid) & (right < mid) # array of bool
    ## cuz checking pair -> at edge will be False automatically
    
    # 1.3 : create pos array (start at 1 cuz we peaks array is n-2 array
    pos_strip = np.arange(1 , x.shape[0] - 1 , 1) # pso array that not include left & right

    # 1.4 : index only True pos.
    return pos_strip[ peaks_strip ] # slice array only True in array

# 2 : main fn -> for input info
def main():
    # input info
    d = np.array([float(e) for e in input().split()])
    # call fn and get array of peak pos.
    pos = peak_indexes(np.array(d))
    # check length of array
    if len(pos) > 0:
        print(", ".join([str(e) for e in pos])) # join each element
    else:
        print("No peaks")

# 3 : execute fn
exec(input())