# create 4 fns
# 1 : row_number -> return row nb. if found element in sublist
def row_number(t,e) :
    found = False
    for i in range(len(t)) :
        for j in range(len(t[i])) :
            # if found e -> return i
            if t[i][j] == e :
                found = True
                return i # top row = 0 -> return i
            
# 2 : flatten -> decompose list (of list) to list (of int)
def flatten(t) :
    list_out = [] # list of int
    for i in range(len(t)) : # t[i] = sublist
        for j in range(len(t[i])) :
            if t[i][j] != 0 : 
                list_out.append(t[i][j])
    # out of loop
    return list_out

# 3 : inversion -> check pair (12 13 14 .. 17 18 , 23 24 , ... , 78)
def inversions(x) :
    count_inversion = 0 # define count
    for i in range(len(x) - 1) : # no need last ele
        for j in range(i+1 , len(x)) : # start inner loop at id 1
            # note : slice until last char = len(8) - 1 = 7 (1,2,3,4,5,6)
            if x[i] > x[j] : # compare
                count_inversion += 1
    # out of loop
    return count_inversion

# 4 : solvable -> check condition from table
def solvable(t) :
    # 4.1 : call function we need to use
    row_0 = row_number(t , 0) 
    list_flatten = flatten(t) # result from calling fn
    count_inv = inversions(list_flatten) # result from calling fn
    
    # case 1 : #row = odd , #inversion = even (no need to check 0 in any index)
    if (len(t) % 2 != 0) and (count_inv % 2 == 0) :
        return True
    
    # case 2 : #row = even , #inversion = odd , 0 in even row
    if (len(t) % 2 == 0) and (count_inv % 2 != 0) and (row_0 % 2 == 0) :
        return True
    
    # case 3 : #row = even , #inversion = even , 0 in odd row
    if (len(t) % 2 == 0) and (count_inv % 2 == 0) and (row_0 % 2 != 0) :
        return True
    
    # otherwise -> return False
    return False

# 5 : execute fn
exec(input().strip())
        
    