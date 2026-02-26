# 1 : input a,b,c,d
a,b,c,d = [int(e) for e in input().split()]

# check d > a
if d > a :
    # yes -> do left
    n = 0
    
    # while loop
    while a < d :
        n = n + 1
        a = a + abs(b)
        d = d - abs(c)
        
    # out of loop -> print n,a,d
    print(n,a,d)
    
else : # do right
    # swap a with d
    a,d = d,a 
    # check cds
    if a > b :
        a,b = b,a
    if c > d :
        c,d = d,c
        
    # check if cds 
    if b == c :
        print(a,b,d)
    else :
        if b > c :
            print((b+c)/2)
        else :
            print(a,b,c,d)