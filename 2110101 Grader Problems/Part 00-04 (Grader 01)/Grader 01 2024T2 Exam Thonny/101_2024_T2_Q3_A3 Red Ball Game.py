# 1 : input info
glass = input().split(',') # split into list
swapped = glass # create list for swapped glass

# 2 : for loop -> swap glass each round
for i in range( int(input()) ) :
    
    # split info -> start pos. & end pos.
    ## -1 for indexing & slicing in list
    start , end = [int(e) for e in input().split()]
    
    # slice list for easier
    left = swapped[0 : start - 1] 
    mid = swapped[end : ]
    right = swapped[start - 1 : end]
    
    # slice index & replace back to swapped
    swapped = left + right + mid
    
# 3 : join list then print
print(','.join(swapped))