# create 2 fns -> BWT & inverseBWT
def BWT(x) : # encode
    # step 1 : append $ to last
    y = x + '$'
    
    # step 2 : create list of str that collect all possible char for rotating each time
    bwt_rotleft = [y]
    for i in range(len(y) - 1) :
        y = y[1:] + y[0] # rotate left 1 pos for each time
        # append each time rotated
        bwt_rotleft.append(y)
        
    # step 3 : sort alphabetically list of rotation
    bwt_rotleft = sorted(bwt_rotleft)
    
    # step 4 : pick last character of each element
    bwt_encode = ''
    for ele in bwt_rotleft :
        bwt_encode += ele[-1]
        
    # step 5 : return encoded str
    return bwt_encode

def inverseBWT(z) : # decode
    # step 1 : split each string to list of str
    z_split = [''] * len(z)
    for i in range(len(z)) : z_split[i] = z[i]
    
    # step 2 : for loop -> add to first pos then sort alphabetically
        # given first list has [''] * len(z)
    bwt_decode = [''] * len(z)
    
    # outer loop : sort with nb. of len(z)
    for j in range(len(z)) :
        # inner loop : add z_split to front of each element
        for i in range(len(bwt_decode)) :
            bwt_decode[i] = z_split[i] + bwt_decode[i]
        # sort list alphabetically
        bwt_decode = sorted(bwt_decode)
        
    # step 3 : remove first char in that element then return
    bwt_decode_result = bwt_decode[0][1:]
    return bwt_decode_result

exec(input().strip())
        