# 1 : input info
a,b,c,d = [int(e) for e in input().split()]

# 2 : check condition
if a == 1 :
    a = b + c + d
    # do left
    if b == 1 :
        c += c + d
    else :
        if b > 4 :
            c += c * d
        # check if
        if b > 5 :
            c += (c % d)
    print(c)
    
else :
    while b < c :
        b += 1
        if b > a :
            break
            
print(a,b,c,d)