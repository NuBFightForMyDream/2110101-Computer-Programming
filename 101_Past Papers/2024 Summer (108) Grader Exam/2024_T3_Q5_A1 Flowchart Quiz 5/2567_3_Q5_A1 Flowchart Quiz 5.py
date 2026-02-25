#
# 2567_3_Q5_A1: 2567_3_Q5_A1: Flowchart 
#

# 1 : input info
a,b,c,d = [int(e) for e in input().split()]

if a == 1 :
    # yes : do left
    c,d = d,c
    
    if b == 1 :
        c += d
    
    elif b < 5 :
        c -= d
        
    elif b <= 10 :
        c /= d
        
# no : do right
else : 
    if a != 10 :
        
        if b > 1 :
            c += d
        if b > 2 :
            c %= d
            
        if b > 3 :
            c += c ** d
        else :
            c -= 1
    
    else :
        while a > d :
            a -= b
            c += 1
            
# print a,b,c,d
print(a,b,c,d)
