def convolute(M,K) : # sum products of same pos. in different matrix
    # M,K = list of list
    
    # define convolution var.
    convolution = 0
    
    # nested for loop
    for row in range(len(M)) : #len M = len K
        for column in range(len(M[row])) : # len M[i] = len K[i]
            convolution += (M[row][column] * K[row][column])
    
    # out of loop -> return result
    return convolution

# execute input
exec(input())            
        
    