# import numpy first
import numpy as np

# create fns
def toCelsius(fahrenheit) : # change deg_F to deg_C
    # f is already array 1D (no need to array() again)
    # calculate each index -> use formula (5/9 * F-32)
    celsius_array = (5/9) * (fahrenheit - 32) # we can multiply array like this
    # return array
    return celsius_array
    
def BMI(wh) :
    # wh = array 2D (n row , 2 col) -> (w1 , h1)
    
    # define BMI (output array) 
    BMI = np.zeros(wh.shape[0]) # 1D array -> we need row = .shape[0] (row , col)
        # make it zeros first then replace value (ndarray can be used (will generate random value))
    
    # replace BMI with new value (index in wh array)
    BMI[ : ] = wh[:,0] / (wh[:,1] / 100) ** 2
    # wh[:,0] = need all row , col 0 (weight kg) in wh array
    # wh[:,1] = need all row , col 1 (height cm) -> / 100 for metre first
    # replace it then calculate
    
    # return array
    return BMI

def distanceTo(p , Points) :
    # p is 1D array (n row , 2 col) -> (xi , yi)
    # Points = 2D array -> storing all (xi,yi) coordinateds
    
    # define 1D array output (storing distance)
    distance = np.ndarray(Points.shape[0]) # shape = row of points (nb. of coordinates)
        # we need row of array -> .shape[0]
    
    ## define var. for easier terms
    # replace distance with new value (calculate each element)
    dx = (Points[: , 0] - p[0]) # array - int => broadcast then minus
    dy = (Points[: , 1] - p[1]) # choose col1 in every row -> do op.
        # dx , dy are array 1D of coordinates
        
    # index all index in distance -> replace new val
    distance[:] = np.abs( np.sqrt(dx**2 + dy**2) ) # abs(sqrt(dx^2 + dy^2))
    
    return distance

# execute fn
exec(input().strip())