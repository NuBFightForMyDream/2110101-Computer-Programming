def factor(N) :
    # 1 : define count & big list 
    count = 0
    prime_factor = []
    
    # 2 : check if N <= 1 -> return immediately
    if N < 1 :
        return 'No Prime Factors'
    
    # 3 : for loop : start form 2 until number
    for fac in range(1 , N+1) :
        
        if fac == 1 :
            N = N / fac # change N 
            count += 1 # add count 
        
        # case 1 : divided -> add count & change N
        elif fac >= 2 :
            # for casse N == 1 : reset count to 0
            count = 0
            # while loop
            while N % fac == 0 :
                N = N / fac # change N 
                count += 1 # add count
            
        # case 2 : not divided -> add old value then reset
        ## for case new value -> check if count >= 1 (count will reset to 0 if old value divided)
        if N % fac != 0 and count >= 1 :
            prime_factor.append([fac , count]) # append sublist to list
            count = 0 # reset count
            
        # check if N is changed to 1 : break immediately
        if N == 1 :
            break
     
    # 4 : out of loop : return list (of list)
    return prime_factor

# 5 ; execute fn
exec(input().strip())