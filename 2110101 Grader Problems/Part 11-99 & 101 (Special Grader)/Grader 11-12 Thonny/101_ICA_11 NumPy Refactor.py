## Sol 1 : using for loop for NumPy Functions
## To-do : change all fucntions by not using loop , recursive , etc.

# 1 : import numpy
import numpy as np

# fn 1 : multiply M (array) with c
def f1(M , c) : # M = 2D array , c = float
    # 1 : create A (array of 0s like M)
    A = np.zeros_like(M)
    # 2 : nested for loop : multiply each pos with C
    for row in range(M.shape[0]) :
        for col in range(M.shape[1]) :
            # 3 : replace new value in each index
            A[row][col] = M[row][col] * c
            
# fn 2 : mutilply 1D array together -> find sum
def f2(U , V) : # U,V are 1D array (equal size)
    d = 0 # sum of array
    # 1 : for loop : sum each products
    for i in range(len(U)) :
        d += U[i] * V[i]
    return d # return when out of loop

# fn 3 : transpose matrix
def f3(M) : # M = 2D array
    # 1 : create ndarray with transpose shape
    t = np.ndarray(M.shape[::-1]) # transpose shape
    # 2 : nested for loop -> replace value
    for col in range(M.shape[1]) :
        for row in range(M.shape[0]) :
            t[row , col] = M[col , row] # choose index in array
    # 3 : out of loop -> return t
    return t

# fn 4 : find vector (cos , sin) for point in radius
def f4(x ,y , dx , dy , k , R):
    # x,y is coordinates 
    
    
    
    
    
    
    