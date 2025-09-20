# 1 : input a,b,c,d
a,b,c,d = [int(e) for e in input().split()]

# 2 : check condition
if a > 1 : # yes -> do right
    while b < d :
        b = b + 1
        if b > c :
            c = c + 3
        else :
            break
    
else : # no -> do left
    a = b + c + d
    if b > 7 : # yes -> do left
        if b > 9 :
            c = 2*d + 2
            # check b > 12
            if b > 12 :
                c = 4*d
            if b > 15 :
                d = c - a
            else : # b <= 15
                d = c + 2*a
            print(c,d)
        else :
            c = 3*d
    # no -> do left
    else :
        if b > 5 :
            b = c + d
        else :
            if b > 2 :
                b = 2*c
            else :
                b = c - d
        print(a,b)
    
# print a,b,c,d
print(a,b,c,d)     