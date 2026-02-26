## Past papers : 2562 T1 Grader

# 1 : input a,b,c,d
a = int(input()) ; b = int(input())
c = int(input()) ; d = int(input())

# 2 : check a == 1
if a == 1 :
    d = d / ( b + d / (c + (d / (b*c))) )
    
else :
    if a == 2 :
        # check if b is odd
        if b % 2 != 0 :
            # yes : check if c < 0
            if c < 0 :
                d += (b + c)
        else :
            if c > 0 :
                d += (c - b)
            d -= (b % c)
        
        # multiply d by 2
        d = 2 * d
        
    else :
        if a == 3 :
            pass
        else :
            while a > 0 :
                d += 1
                if d > 10 :
                    break
                else :
                    a = a // 2
                
# round d
print( round(d , 6) )
                