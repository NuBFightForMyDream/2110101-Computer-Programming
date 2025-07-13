#
# 2567_3_Q2_A1: 2567_3_Q2_A1: Flowchart 
#

# input
a,b,c,d = [int(e) for e in input().split()]

if a > b :
    # yes : do right
    if b < 0 :
        c,d = d,c
    else : # b >= 0
        if b > 5 :
            c -= d
        if b < 3 :
            if b < 2 :
                c //= d
            else :
                c *= d
        else : # b >= 3
            c += d
            c *= d
            
else :
    while a > d :
        b += 1
        a -= 1
        d += c
        
print(a,b,c,d)
        
            