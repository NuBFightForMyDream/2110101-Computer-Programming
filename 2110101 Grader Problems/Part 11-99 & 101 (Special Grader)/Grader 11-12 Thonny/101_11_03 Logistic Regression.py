# import numpy
import numpy as np

# define fn
def p( X ) : # predict prob. of passing subjects
    # X is 2D array (n,2) -> [task_done , gpa]
    
    # define var.
        # 1 : for output
    logistic = np.ndarray(X.shape[0]) # 1D array -> shape = row of X 
    prob = np.ndarray(X.shape[0])
        # 2 : for easier terms
    task_done = X[ : , 0] # array for task_done
    gpa = X[ : , 1] # array for gpa
    
    # calculate prob. -> replace new val in empty array
    logistic[ : ] = -3.98 + 0.1 * task_done + 0.5 * gpa
    
    # calculate prob -> replace val.
    prob[ : ] = 1 / ( 1 +  np.e ** -(logistic) )
    
    # return prob array
    return prob

# execute fn
exec(input().strip())