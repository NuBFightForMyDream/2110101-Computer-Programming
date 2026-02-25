#
# 2567_3_Q1_A1: 2567_3_Q1_A1: Flowchart 
#

# import math library
import math

# input info
a,b,c,d,e = [int(e) for e in input().split()]

if a >= e :
    i = 0 ; n = 4
    while i <= n :
        if a >= b :
            a,b = b,a
        if b >= c :
            b,c = c,b
        if c >= d :
            c,d = d,c
        if d >= e :
            d,e = e,d
        i = i + 1
    # out of loop
    print(a,b,c,d,e)
    
else :
    if a == 1 :
        # check b >= c
        if b >= c :
            b,c = c,b
        if c >= d :
            c,d = d,c
        if d >= e :
            d,e = e,d
        # 2 ways
        if b <= c :
            if b <= d :
                print( (c+d)/2 )
            else :
                print( (b+c)/2 )
        else :
            if c <= d : 
                print( (b+d) / 2 )
            else :
                print( (b+c) / 2 )

    else :
        ans = math.sqrt(b**2 + c**2 + d**2) / (a**2)
        print( round(ans , 2) )