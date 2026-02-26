# 1 : input a,b,c,d,e
a,b,c,d,e = [int(e) for e in input().split()]

# 2 : check e
if e >= 6 :
    # yes : do right
    a = 1 ; b = 1 ; c = 0 ; p = 10
    # while loop
    while abs(p - (b/a) ) >= 10**(-e) :
        p = b/a
        a,b = b , a+b
        c = c + 1
        
    # out of loop
    print(b,c)
    
else : # no , do right
    # check if a >= b
    if a >= b :
        # yes : do left
        if c >= d :
            print(a+b+c+d)
        else :
            d , a , b , c = a , b , c , d
            print(a,b,c,d)
            
    # no : do right
    else :
        e = a*3600 + b*60 + c + d
        e = e % (24*60*60)
        a = e // 3600
        b = ( e - a*(3600) ) // 60
        c = e % 60
        
        print(a,b,c)