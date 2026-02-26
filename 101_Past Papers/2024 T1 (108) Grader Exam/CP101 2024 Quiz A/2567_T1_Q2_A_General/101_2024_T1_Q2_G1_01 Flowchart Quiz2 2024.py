# 1 : input a,b,c,d
a,b,c,d = [int(e) for e in input().split()]

# check condition
if a == 1 : 
    a = b+c+d 
    if b > 5 : # yes -> do col2
        if b > 9 : 
            c = 4*d
        else : 
            if b > 7 : 
                c = 5*d
            else : 
                c = 6*d
    else : # do col 1
        if b > 3 : 
            c = 1*d
        else : 
            if b > 0 : 
                c = 2*d
            else : 
                c = 3*d

else : # do col 3
    while b < c :
        b += 1
        if b > a :
            a += c
        # must do c -= 1
        c -= 1
        
# print a,b,c,d
print(a,b,c,d)