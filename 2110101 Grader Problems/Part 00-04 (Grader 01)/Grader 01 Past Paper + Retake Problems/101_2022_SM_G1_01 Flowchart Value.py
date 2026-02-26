# 1 : input a,b,c
a,b,c = [int(e) for e in input().split()]

# 2 : check abs(a) > abs(b)
if abs(a) > abs(b) :
    # yes -> do left
    r = 0 ; s = 0
    ta = abs(a) ; tb = abs(b)
    
    # check while loop
    while ta > tb :
        ta -= tb ; s += 1
        
    # out of loop
    r = ta
    
    # check pair (+ or -)
    if (a > 0 and b > 0) or (a < 0 and b < 0):
        pass
    else : # not -> multiply -1
        s = -s ; r = -r
        
    print(a,b,s,r)
    
# no -> do right
else :
    if (b > 0 and c > 0) or (b < 0 and c < 0) :
        # yes -> do left
        p = 0
        tc = abs(c)
        # for loop
        for i in range(tc) :
            p += abs(b)
        
    else : # do right
        
        p = abs(b)
        tc = abs(c)
        
        # while loop
        while tc > 0 :
            p += abs(b)
            tc -= 1
            
        # out of loop
        p = -(p - abs(b))
    
    print(b,c,p)