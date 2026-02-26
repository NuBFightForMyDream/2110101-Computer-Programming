# 1 : input first
a,b,c,d,e = [int(e) for e in input().split()]

# 2 : check e == 1 ?
if e == 1 : # do left side
    if a < b :
        a , b = b , a
    if c < d :
        c , d = d , c
    if a >= c :
        # yes : do left
        if b >= c :
            print(b)
        else :
            print(c)
    else :
        if a >= d :
            print(a)
        else :
            print(d)
            
else : # do right side
    while e < 3 :
        if a >= b :
            a,b = b,a
        if b >= c :
            b,c = c,b
        if c >= d :
            c,d = d,c
        # increment e by 1
        e += 1
    # out of loop -> print b
    print(b)
            
